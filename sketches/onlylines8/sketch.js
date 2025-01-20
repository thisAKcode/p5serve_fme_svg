const w=720;
const N = 8;
const d=w/N;
const setcol=[]
setcol[0]=["#ef233c", "#fcd5ce"];
setcol[1]=["#eddcd2", "#343a40"];

function setup() {
   createCanvas(w, w);
   ellipseMode(CORNER);
   noFill();
   strokeWeight(d/36);

   col = random(setcol);
   noLoop();
}

function draw() {
   background(col[0]);
   for(let i=0;i<2*N+1;i++){
      const x = d*i/2;
      const dy = (i%2==1) ? d*sqrt(3)/2 : 0;
      for(let j=0;j<N;j++) {
         const y = d*j *sqrt(3) ;
         push();
         translate(x, y+dy);
         pattern(0, 0, d);
         pop();
      }
   }
}

function pattern(x, y, size, mode){
   const l = size/sqrt(3);
   const points = [];
   for(let i=0;i<3;i++){
      const r = TWO_PI/3*i+PI/6;
      point[i] = [l*cos(r), l*sin(r)];
   }
   for(let i=0;i<3;i++){
      const r = TWO_PI/3*i+PI/6 + PI;
      point[i+3] = [l*cos(r), l*sin(r)];
   }

   push();
   stroke(col[1]);
translate(x, y + l/2);
     triangle(...point[0], ...point[1], ...[0, 0]);
     triangle(...point[1], ...point[2], ...[0, 0]);
     triangle(...point[2], ...point[0], ...[0, 0]);
   pop();
   push();
   stroke(col[1]);
   translate(x, y+l/2);
       triangle(...point[3], ...point[4], ...[0, 0]);
       triangle(...point[4], ...point[5], ...[0, 0]);
       triangle(...point[5], ...point[3], ...[0, 0]);
   pop();
}