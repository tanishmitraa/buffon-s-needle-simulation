## 📖 Description

This is a simple simulation of **Buffon’s Needle problem**.  
You drop a needle of length `L` randomly on a plane with parallel lines spaced `d` apart.  
If the needle crosses a line, we count it.  
The ratio of total drops to crossings gives an estimate of π using:

π ≈ (2 * L * N) / (d * C)

- `N` = number of needle drops  
- `C` = number of times the needle crosses a line  

Basically, the more samples you run, the closer you get to π.  
For small samples, it’s noisy as hell and might not even cross at all.  
But with large `N`, it converges nicely.  

The script shows two plots:  
1. How the π estimate converges as you drop more needles.  
2. A visual of the needle drops (green = cross, blue = no cross, dashed = lines).
