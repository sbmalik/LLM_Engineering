
## Does  real life derivatives always have time as the moving part?
No. Time is just the most common one, because "how fast is this changing" usually means "per second" or "per year" in everyday speech. A derivative is really "how much does this respond when I nudge that", and that can be anything.

Some real ones where nothing is moving in time:

- Slope of a road. Height per metre travelled. Nobody is driving; the hill just has a steepness at every point. A gradient sign saying 8% is literally a derivative.
- Marginal cost. How much the total cost of a factory goes up per extra unit produced. The variable is "number of units", not time. Economists use derivatives with respect to quantity, price and income all day long.
- Price sensitivity. How many fewer people buy per euro of price increase.
- Sensitivity of a recipe. How much sweeter a cake gets per extra spoon of sugar.
- Temperature across a wall. Degrees per centimetre from the warm side to the cold side; this is what decides how fast heat leaks through.
- Medicine. Change in effect per milligram of dose.

## Functions that don't have derivatives
- the functions which have breakages or sharp turns or corners don't have derivates at all and it is because thef delta-x is coming from the right is different from the delta-x coming from the left and tangent line (slope) changes immediately. For example ReLU @ 0
- Verticle tangents: because a vericle line has infinite derivative possibilities and infinity is not a real number 
- Can I assign one finite slope to the tangent at this point?" if Yes => differentiable, if No => not differentiable
- | Situation          | What happens?                           | Derivative?     |
| ------------------ | --------------------------------------- | --------------- |
| Smooth curve       | One clear tangent                       | ✅ Exists        |
| Corner (ReLU at 0) | Left/right slopes differ                | ❌ Doesn't exist |
| Vertical tangent   | Slope becomes infinitely steep          | ❌ Doesn't exist |
| Gap/discontinuity  | Function isn't properly connected there | ❌ Doesn't exist |
 