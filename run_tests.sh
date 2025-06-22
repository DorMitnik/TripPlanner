#!/bin/bash
echo "Running backend tests..."
docker exec tripplanner-backend-1 pytest /app/test_main.py

echo "Running frontend tests..."
docker exec tripplanner-frontend-1 npm test -- --watchAll=false
