# NPAW Video Analytics Integration

This repository contains a collection of test implementations and examples for integrating NPAW (Nice People At Work) video analytics with VideoJS players. The project is organized into two main sections: API tests and integration tests.

## Project Structure

### API Tests (`ApiTest/`)
Contains examples of interacting with the NPAW API:
- `part1/`: Basic API request implementation with token generation
- `part2/`: VideoJS integration with NPAW plugin and custom bitrate handling

### Integration Tests (`IntegrationTest/`)
Contains different implementations of video player integrations:
- `part1/`: Basic HTTPS server setup with VideoJS and NPAW plugin. The JSON adapter provided throws a not supported error, due to time contraints we are getting the adapter from artifactory
- `part2/`: Enhanced implementation with custom adapter for bitrate conversion
- `part3/`: Allow the user to select dynamically how the bitrate should be reported (bits or Mbps).

## Features

- VideoJS player integration with NPAW analytics
- Custom bitrate handling (bits/Mbps conversion)
- HTTPS server support with SSL certificates
- CORS-enabled endpoints
- Real-time video analytics tracking
- Buffer health monitoring
- Playback quality metrics

## Getting Started

1. Install dependencies:
```bash
npm install
```

2. Start the server:
```bash
npm start
```

3. Access the demo at `https://localhost:3000` (for HTTPS) or `http://localhost:3000` (for HTTP)

## Configuration

The project uses the following key configurations:
- Account code: `/powerce`
- API key: Configured in the respective implementation files
- Default port: 3000

## Dependencies

- Express.js
- VideoJS
- NPAW Plugin
- HLS.js

## Security Note

The repository includes SSL certificates for development purposes. For production use, ensure you have proper SSL certificates and secure API key management. 