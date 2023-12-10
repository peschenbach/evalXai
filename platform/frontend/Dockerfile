# Use official Node.js image as base image
#FROM node:20 AS frontend

# Set the working directory within the container
#WORKDIR /app
#COPY package*.json ./
#RUN npm install
#COPY . .

# Build the Next.js app
#RUN npm run build

FROM node:18

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD npm run dev