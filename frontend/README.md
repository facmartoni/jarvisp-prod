# Frontend

React + TypeScript frontend with Apollo Client for GraphQL.

## Setup

1. Install dependencies:
```bash
pnpm install
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Start development server:
```bash
pnpm dev
```

## Available Scripts

- `pnpm dev` - Start development server
- `pnpm build` - Build for production
- `pnpm preview` - Preview production build
- `pnpm lint` - Run ESLint

## GraphQL Integration

Apollo Client is configured in `src/apollo-client.ts`.

### Example Query

```typescript
import { useQuery, gql } from '@apollo/client'

const GET_DATA = gql`
  query GetData {
    hello
  }
`

function Component() {
  const { loading, error, data } = useQuery(GET_DATA)
  
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error: {error.message}</p>
  
  return <div>{data.hello}</div>
}
```

### Example Mutation

```typescript
import { useMutation, gql } from '@apollo/client'

const CREATE_ITEM = gql`
  mutation CreateItem($name: String!) {
    createItem(name: $name) {
      id
      name
    }
  }
`

function Component() {
  const [createItem] = useMutation(CREATE_ITEM)
  
  const handleSubmit = () => {
    createItem({ variables: { name: 'New Item' } })
  }
  
  return <button onClick={handleSubmit}>Create</button>
}
```

## Environment Variables

See `.env.example` for required variables.

All Vite environment variables must be prefixed with `VITE_`.
