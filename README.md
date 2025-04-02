# URL Shortener Microservice - Week 1   
**Containerized Implementation with Flask and Redis**
## Objective  
Developed and containerized a basic URL shortener service that:  
1. Accepts long URLs via REST API  
2. Generates and returns shortened URLs  
3. Redirects users from short URLs to original URLs  
4. Uses Redis for persistent key-value storage  
5. Runs in isolated Docker containers  

## How to run:
1. docker build -t url-shortener .
2. docker-compose up
3. curl -X POST -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}' http://localhost:5001/shorten

# Week-2
