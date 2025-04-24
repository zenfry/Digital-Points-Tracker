import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useState } from "react";

const initialHouses = [
  { name: "Talon of Insight", color: "#4B0082", points: 0 },
  { name: "Talon of Flame", color: "#B22222", points: 0 },
  { name: "Talon of Stone", color: "#228B22", points: 0 },
  { name: "Talon of Sky", color: "#87CEEB", points: 0 },
];

export default function HousePointsTracker() {
  const [houses, setHouses] = useState(initialHouses);

  const adjustPoints = (index, delta) => {
    const newHouses = [...houses];
    newHouses[index].points += delta;
    setHouses(newHouses);
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
      {houses.map((house, index) => (
        <Card key={house.name} style={{ borderLeft: `8px solid ${house.color}` }}>
          <CardContent className="flex flex-col items-start space-y-4 p-4">
            <h2 className="text-xl font-bold" style={{ color: house.color }}>{house.name}</h2>
            <p className="text-3xl font-semibold">{house.points} pts</p>
            <div className="flex gap-2">
              <Button onClick={() => adjustPoints(index, 5)}>+5</Button>
              <Button onClick={() => adjustPoints(index, 10)}>+10</Button>
              <Button onClick={() => adjustPoints(index, -5)} variant="destructive">-5</Button>
              <Button onClick={() => adjustPoints(index, -10)} variant="destructive">-10</Button>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
