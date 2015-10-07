# This data file was generated by SCIM.
# You almost certainly shouldn't edit it.

format A 10 0 0
format B 13 2 0
format C 23 2 0
format D 21 2 0
format E 10 4 0
leftstring A0 = "Messung"
leftstring B0 = "Laufzeit (ms)"
leftstring C0 = "Differenz zu Mittelwert"
leftstring D0 = "Quadrat der Differenz"
let A1 = 1
let B1 = 7.59
let C1 = B1-B23
let D1 = C1^2
let A2 = A1+1
let B2 = 7.16
let C2 = B2-B23
let D2 = C2^2
let A3 = A2+1
let B3 = 6.97
let C3 = B3-B23
let D3 = C3^2
let A4 = A3+1
let B4 = 7.55
let C4 = B4-B23
let D4 = C4^2
let A5 = A4+1
let B5 = 6.77
let C5 = B5-B23
let D5 = C5^2
let A6 = A5+1
let B6 = 6.97
let C6 = B6-B23
let D6 = C6^2
let A7 = A6+1
let B7 = 7.74
let C7 = B7-B23
let D7 = C7^2
let A8 = A7+1
let B8 = 7.18
let C8 = B8-B23
let D8 = C8^2
let A9 = A8+1
let B9 = 7.32
let C9 = B9-B23
let D9 = C9^2
let A10 = A9+1
let B10 = 7.7
let C10 = B10-B23
let D10 = C10^2
let A11 = A10+1
let B11 = 7.4
let C11 = B11-B23
let D11 = C11^2
let A12 = A11+1
let B12 = 7.58
let C12 = B12-B23
let D12 = C12^2
let A13 = A12+1
let B13 = 7.04
let C13 = B13-B23
let D13 = C13^2
let A14 = A13+1
let B14 = 7.17
let C14 = B14-B23
let D14 = C14^2
let A15 = A14+1
let B15 = 6.89
let C15 = B15-B23
let D15 = C15^2
let A16 = A15+1
let B16 = 7.2
let C16 = B16-B23
let D16 = C16^2
let A17 = A16+1
let B17 = 7.33
let C17 = B17-B23
let D17 = C17^2
let A18 = A17+1
let B18 = 7.21
let C18 = B18-B23
let D18 = C18^2
let A19 = A18+1
let B19 = 8.05
let C19 = B19-B23
let D19 = C19^2
let A20 = A19+1
let B20 = 7.63
let C20 = B20-B23
let D20 = C20^2
leftstring A22 = "Sum:"
let B22 = @sum(B1:B20)
leftstring A23 = "Average:"
let B23 = B22/20
leftstring A25 = "Summe der Fehlerquadrate:"
let D25 = @sum(D1:D20)
leftstring A27 = "Fehler des Mittelwertes"
let D27 = D25/(20*10)
leftstring A29 = "Expected speed of sound (meters per second):"
let D29 = 331.3+0.606*23
leftstring A30 = "see Wikipedia, Speed of Sound"
leftstring A33 = "Length of test path (meter):"
let D33 = 2.561
leftstring A34 = "Uncertainty of test path length (meters)"
let D34 = 0.003
leftstring A37 = "average speed (meters per second):"
let D37 = D33/B23*1000
leftstring A40 = "Gauss'sches Fehlerfortpflanzungsgesetz"
let D40 = @sqrt((1/(B23/1000)*0.003)^2+(-1*2.561/(B23/1000)^2*D27)^2)
leftstring A42 = "Erster Term, GFFPG"
let D42 = 1/(B23/1000)*0.003
leftstring A43 = "Zweiter Term, GFFFP"
let D43 = -1*2.561/(B23/1000)^2*D27/1000
leftstring A44 = "Quadrat erster Term"
let D44 = D42^2
leftstring A45 = "Quadrat, zweiter Term"
let D45 = D43^2
leftstring A46 = "Summe der Quadrate"
let D46 = D44+D45
leftstring A47 = "Quadratwurzel"
let D47 = @sqrt(D46)
let E47 = @sqrt(D46)
goto E47