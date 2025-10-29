# Data Models Documentation

This document describes the data models for the JarvISP customer service AI bot application.

## Model Relationships

See the UML diagrams in the backend directory:
- `models_diagram.png` - Standard model diagram
- `models_diagram.svg` - SVG version (scalable)
- `models_diagram_detailed.png` - Detailed view with all Django built-in models
- `models_diagram_with_cascade.png` - Color-coded by deletion behavior

## Generating Diagrams

To regenerate the UML diagrams:

```bash
# Standard diagram
uv run python manage.py graph_models api -o models_diagram.png

# SVG version
uv run python manage.py graph_models api -o models_diagram.svg

# With all Django apps
uv run python manage.py graph_models api --all-applications -g -o models_diagram_detailed.png

# Color-coded deletion behaviors
uv run python manage.py graph_models api --color-code-deletions --arrow-shape crow -o models_diagram_with_cascade.png
```

## Model Overview

### Core Models

1. **Company** - Multi-tenant organization
   - Central model for all data
   - Has timezone, WhatsApp integration
   - Related to: Customer, Conversation, ISPCubeIntegration, BillingEvent, KnowledgeBase, Template

2. **Customer** - End users/clients
   - N:1 to Company
   - E.164 phone validation
   - Unique phone per company
   - Related to: Conversation

3. **Conversation** - Chat sessions
   - N:1 to Company
   - N:1 to Customer
   - Has status flow (NEW → BOT_ACTIVE → ESCALATED → TRANSFERRED → RESOLVED → CLOSED)
   - Related to: Message, AgentHandoff, Feedback

4. **Message** - Individual messages
   - N:1 to Conversation
   - Has role (User, Assistant, Agent, System)
   - Tracks tokens and latency
   - Related to: ToolCallLog

### Integration Models

5. **ISPCubeIntegration** - ISPCube API configuration
   - N:1 to Company
   - Encrypted credentials (password, api_key, api_token)
   - Token expiration tracking

### AI/Bot Models

6. **ToolCallLog** - LLM function calls
   - N:1 to Message
   - Tracks tool execution (arguments, response, duration, success)

7. **KnowledgeBase** - Bot knowledge entries
   - N:1 to Company
   - Question/answer pairs with keywords
   - Category-based organization

8. **Template** - Reusable message templates
   - N:1 to Company
   - Trigger keywords
   - Usage tracking

### Support Models

9. **AgentHandoff** - Human agent escalations
   - N:1 to Conversation
   - Tracks escalation reason, assigned agent, resolution

10. **Feedback** - Customer satisfaction
    - 1:1 to Conversation
    - Rating (1-5 stars)
    - Resolution tracking

### Billing Models

11. **BillingEvent** - Usage and subscription billing
    - N:1 to Company
    - Types: Subscription, Overage
    - Auto-calculates total_amount

## Key Features

- **Encryption**: ISPCube credentials encrypted with Fernet
- **Phone Validation**: E.164 format with phonenumbers library
- **Soft Deletes**: PROTECT on most relationships to prevent data loss
- **Indexes**: Optimized for common queries
- **JSON Fields**: Flexible metadata and keywords storage
- **Unique Constraints**: Phone/external_id unique per company
- **Timestamps**: Auto-tracked created_at/updated_at on all models

## Database Indexes

All models have strategic indexes for query performance:
- Conversation: (company, customer, is_active), (company, last_message_at), (customer, created_at)
- Message: (conversation, created_at), (conversation, role)
- ToolCallLog: (message, created_at), (tool_name, success)
- Customer: (company, phone), (company, external_id) via unique_together
- And more...

