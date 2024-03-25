# Frontend Documentation

## Overview

The frontend of the Explainable AI Benchmarking Platform is responsible for providing a user-friendly interface for users to interact with the platform. It handles the presentation layer and user interactions.

It is built using Next.js, a React framework for production.

## Technologies Used

- HTML
- CSS
- JavaScript
- React.js
- Next.js

## Libraries Used

- [Material-UI]
- [Axios]
- [Tailwind-CSS]
- [React-Router-DOM]

## Getting Started

First install the dependencies:

```bash
npm install
# or
yarn
```

Secondly, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Pages

### App

- home page

### competition page

- list of competitions
- competition details
- leaderboard

### datasets page

- list of datasets
- dataset details

## Components

- Header:
  This component displays the header section of the platform, including the logo, search bar, and navigation links.

- File Upload: Component for uploading a file and displaying upload status, score, and error. It uses Axios

- LeaderBoard : Renders a leaderboard table component. @returns The leaderboard table component.

- SingleCompetition: Renders a single competition component.

- TemporaryDrawer: Renders a temporary drawer component. It functions as a sidebar when clicking the menu icon in the header.

- Footer: Renders the footer component.
