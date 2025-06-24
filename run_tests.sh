#!/bin/bash
echo "Running backend tests..."
docker exec tripplanner-backend-1 pytest /app/test_main.py
