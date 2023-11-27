# FRONTEND
# Use official Node.js image as base image
FROM node:14 AS frontend

WORKDIR /app/frontend
COPY frontend/package*json ./
RUN npm install
COPY frontend/ .

# Build the Next.js app
RUN npm run build

# BACKEND
# Use official Python image as base image
FROM python:3.10 AS backend

WORKDIR /app/backend
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .

# Expose the Django server port
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use a smaller base image for the final image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the built frontend from the "frontend" stage
COPY --from=frontend /app/frontend/build ./frontend/build

# Copy the installed backend from the "backend" stage
COPY --from=backend /app/backend .

# Expose the Django server port
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Building and runing
# Run the following commands in the project directory
# "docker-compose build"
# "docker-compose up"