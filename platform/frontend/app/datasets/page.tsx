import React from "react";
import Header from "@/app/components/Header";
import {
  Card,
  CardActionArea,
  CardContent,
  CardMedia,
  Typography,
} from "@mui/material";
import Link from "next/link";
import tetris from "@/public/tetris.png";

const Datasets = () => {
  const competitionName = "Tetris";
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex flex-1 flex-col items-center justify-center p-24 bg-gray-300">
        <h1 className="text-4xl font-bold mb-4">Datasets</h1>
        <p className="my-10">
          In the following you can see all available datasets. Click on the
          cards to learn more.
        </p>
        <Link href={`/datasets/tetris`} passHref>
          <Card sx={{ maxWidth: 345, cursor: "pointer" }}>
            <CardActionArea>
              <CardMedia
                component="img"
                sx={{
                  height: 230,
                }}
                height="140"
                image={tetris.src}
                alt="Tetris"
              />

              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  {competitionName} Dataset
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Click here to learn more and view the tetris explainable AI
                  dataset.
                </Typography>
              </CardContent>
            </CardActionArea>
          </Card>
        </Link>
      </main>
      <footer className="w-full bg-gray-800 text-white text-center p-4">
        <p>© 2023 A TUB Project - Explainable AI Project.</p>
      </footer>
    </div>
  );
};

export default Datasets;
