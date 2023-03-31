# Tiktoken Counter API

The Tiktoken API is a tool that enables developers to calculate the token usage of their OpenAI API requests before sending them, allowing for more efficient use of tokens.

## Docker
```bash
docker run -d -p 8000:8000 enrikenur/tiktoken:latest
```

## Usage

/count sample payload:

> Available models: gpt-3.5-turbo, gpt-4

```json
 {
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "This late pivot means we don't have time to boil the ocean for the client deliverable."
    }
  ]
}
```
Response:
```json
{
	"count":  27
}
```
    
CURL Request:
```bash
curl --location 'http://127.0.0.1:8000/count' \
	--header 'Content-Type: application/json' \
	--data  '{
		"model": "gpt-3.5-turbo",
		"messages": [
			{
				"role": "user",
				"content": "This late pivot means we don\'t have time to boil the ocean for the client deliverable."
			}
		]
	}'
```

## License

The Tiktoken API is licensed under the MIT License. See the `LICENSE` file for more details.
