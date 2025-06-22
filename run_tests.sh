#!/bin/bash
echo "Running backend tests..."
docker exec tripplanner-backend-1 pytest /app/tests

echo "Running frontend tests..."
docker exec tripplanner-frontend-1 npm test -- --watchAll=false
