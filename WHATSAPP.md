# WhatsApp Business API Guide

## 24-Hour Messaging Window Rule

WhatsApp has strict rules about when you can send messages:

### Business-Initiated Conversations

**❌ CANNOT send regular text messages first**
**✅ MUST send a template message first**

```
Business → Customer: Template (e.g., hello_world)
Customer → Business: Any message
Business → Customer: Regular text messages (24h window opens)
```

**Example:**
```python
# First contact - MUST use template
send_template(to='54381156378744', template='hello_world')

# After customer replies, you can send regular messages
send_message(to='54381156378744', text='Thanks for your response!')
```

### Customer-Initiated Conversations

**✅ CAN send regular text messages immediately**
**❌ NO template required**

```
Customer → Business: Any message (webhook receives it)
Business → Customer: Regular text messages (24h window is already open)
```

**Key Point:** If the customer speaks first, the 24-hour window opens automatically. No template needed!

### The 24-Hour Window

- Opens when customer sends a message OR responds to a template
- Closes 24 hours after the last customer message
- During this window: send unlimited regular text messages
- After window closes: can only send templates until customer responds again

## Phone Number Formats

### Argentina Mobile Numbers

WhatsApp uses a different format than standard E.164 for Argentina mobile numbers:

**E.164 Standard:** `+54` + `9` + `area_code` + `number`
- Example: `+5493816378744`

**WhatsApp Format:** `54` + `area_code` + `15` + `number`
- Example: `54381156378744`

**Our System:**
- **Store in DB:** E.164 format (`+5493816378744`)
- **Send to WhatsApp API:** Original format from webhook (`54381156378744`)
- **Parse incoming:** Add `+` prefix before using phonenumbers library

### Code Example

```python
# Webhook receives: "54381156378744"
# We parse as: "+54381156378744"
# E.164 normalized: "+5493816378744" (stored in DB)
# Send to WhatsApp: "54381156378744" (use original from webhook)
```

## Development Flow

### Problem: One Webhook URL at a Time

Meta only allows ONE webhook URL configured per WhatsApp app.

### Solution: Development Strategies

#### Option 1: Toggle Between Environments

**For Local Development:**
```bash
# Terminal 1: Run local server
cd backend
uv run python manage.py runserver 8001

# Terminal 2: Expose with ngrok
ngrok http 8001
# Copy URL: https://abc123.ngrok.io

# Meta Dashboard: Configure webhook
# URL: https://abc123.ngrok.io/api/whatsapp/webhook
# Verify token: gJWo6B-DUBOhBXO4NHX-N1iB4wLVyAZr1XDvC8nNWI4
```

**For Production Testing:**
```bash
# Meta Dashboard: Switch webhook back
# URL: https://your-app.fly.dev/api/whatsapp/webhook
```

**Pros:** Simple, clear separation
**Cons:** Manual switching, can't test both simultaneously

#### Option 2: Use Different WhatsApp Test Numbers

Create multiple WhatsApp test apps:
- **Dev App:** Points to ngrok URL (for development)
- **Prod App:** Points to production URL (for staging/prod)

**Pros:** No switching, test both environments
**Cons:** Need multiple Meta apps, separate phone numbers

#### Option 3: Webhook Forwarder (Advanced)

Use a proxy service that forwards to multiple URLs:
- Configure Meta webhook to proxy
- Proxy forwards to both ngrok AND production
- Filter by environment variable or request header

**Pros:** Test both simultaneously
**Cons:** More complex setup, potential duplicate processing

### Recommended Flow

**For Active Development:**
1. Use ngrok for webhook during feature development
2. Test with your personal number in the allowlist
3. When stable, switch to production URL
4. Test end-to-end in production

**For Production:**
1. Keep webhook pointed at production URL
2. Monitor logs via `fly logs` or logging service
3. For urgent debugging: temporarily switch to ngrok

## Testing Without Real WhatsApp

### Using curl (No WhatsApp Required)

Simulate webhook payloads locally:

```bash
curl -X POST http://localhost:8001/api/whatsapp/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "object": "whatsapp_business_account",
    "entry": [{
      "changes": [{
        "value": {
          "metadata": {"phone_number_id": "867858046411646"},
          "messages": [{
            "from": "54381156378744",
            "id": "wamid.TEST001",
            "text": {"body": "Test message"},
            "type": "text"
          }]
        }
      }]
    }]
  }'
```

**Note:** This won't send actual WhatsApp messages, but tests:
- Webhook parsing
- Database operations
- Business logic
- Error handling

## Allowlist Management

### Test/Development Mode

WhatsApp apps in test mode require phone numbers to be allowlisted.

**To add numbers:**
1. Meta for Developers → Your App
2. WhatsApp → API Setup
3. "Manage phone number list"
4. Add with format: `54381156378744` (14 digits for Argentina)

### Production Mode

After going live, you can message any WhatsApp user (no allowlist).

**To go live:**
1. Complete Business Verification
2. Submit app for review
3. Get approved
4. Allowlist removed automatically

## Common Issues

### "Recipient phone number not in allowed list"

**Cause:** Number not added to allowlist in Meta dashboard
**Fix:** Add number with exact format from API docs

### "Session has expired"

**Cause:** Access token expired (temporary tokens last 24h)
**Fix:** Generate new access token or set up permanent token

### Template messages work, text messages don't

**Cause:** 24-hour window not open
**Fix:** Wait for customer to respond to template first

### E164 parsing fails

**Cause:** Phone number missing `+` prefix
**Fix:** Add `+` before parsing: `f'+{from_number}'`

## Quick Reference

### Send Template (Business initiates)
```python
# Use when starting conversation
POST /v18.0/{phone_number_id}/messages
{
  "messaging_product": "whatsapp",
  "to": "54381156378744",
  "type": "template",
  "template": {
    "name": "hello_world",
    "language": {"code": "en_US"}
  }
}
```

### Send Text Message (Within 24h window)
```python
# Use after customer responds
POST /v18.0/{phone_number_id}/messages
{
  "messaging_product": "whatsapp",
  "to": "54381156378744",
  "type": "text",
  "text": {"body": "Your message here"}
}
```

### Webhook Payload (Incoming message)
```python
{
  "object": "whatsapp_business_account",
  "entry": [{
    "changes": [{
      "value": {
        "metadata": {"phone_number_id": "867858046411646"},
        "messages": [{
          "from": "54381156378744",
          "id": "wamid.ABC123",
          "text": {"body": "Customer message"},
          "type": "text"
        }]
      }
    }]
  }]
}
```

## Environment Variables

```bash
# Required
WHATSAPP_ACCESS_TOKEN=EAAQi3cpeAgk...
WHATSAPP_VERIFY_TOKEN=gJWo6B-DUBOhBXO4NHX-N1iB4wLVyAZr1XDvC8nNWI4

# Optional (has defaults)
WHATSAPP_API_URL=https://graph.facebook.com/v18.0
```

## Resources

- [WhatsApp Business API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [Message Templates](https://developers.facebook.com/docs/whatsapp/message-templates)
- [Webhook Payload Examples](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/payload-examples)
- [Phone Number Formats](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/phone-numbers)

