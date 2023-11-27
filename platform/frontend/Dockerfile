# Use official Node.js image as base image
FROM node:20 AS frontend

# Set the working directory within the container
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
COPY . .

# Build the Next.js app
RUN npm run build