# This data file was generated by SCIM.
# You almost certainly shouldn't edit it.

format A 15 0 0
format B 12 2 0
format C 12 2 0
format D 19 2 0
format E 19 2 0
format F 21 2 0
format G 13 2 0
format H 13 2 0
format J 10 7 0
leftstring A0 = "Messung"
leftstring B0 = "F (Newton)"
leftstring C0 = "z (Meter)"
leftstring B1 = "xi"
leftstring C1 = "yi"
leftstring D1 = "xi-x_durchschnitt"
leftstring E1 = "yi-y_durchschnitt"
leftstring F1 = "(xi-x_ds)*(yi-y_ds)"
leftstring G1 = "(xi-x_ds)^2"
leftstring H1 = "(yi-y_ds)^2"
leftstring I1 = "y_dach_i"
let A2 = 1
let B2 = 3.83
let C2 = 0.2
let D2 = B2-B14
let E2 = C2-C14
let F2 = D2*E2
let G2 = D2^2
let H2 = E2^2
let I2 = I17*C2+I18
let A3 = A2+1
let B3 = 7.79
let C3 = 0.35
let D3 = B3-B14
let E3 = C3-C14
let F3 = D3*E3
let G3 = D3^2
let H3 = E3^2
let I3 = I17*C3+I18
let A4 = A3+1
let B4 = 8.08
let C4 = 0.42
let D4 = B4-B14
let E4 = C4-C14
let F4 = D4*E4
let G4 = D4^2
let H4 = E4^2
let I4 = I17*C4+I18
let A5 = A4+1
let B5 = 9.7
let C5 = 0.46
let D5 = B5-B14
let E5 = C5-C14
let F5 = D5*E5
let G5 = D5^2
let H5 = E5^2
let I5 = I17*C5+I18
let A6 = A5+1
let B6 = 10.58
let C6 = 0.51
let D6 = B6-B14
let E6 = C6-C14
let F6 = D6*E6
let G6 = D6^2
let H6 = E6^2
let I6 = I17*C6+I18
let A7 = A6+1
let B7 = 12.33
let C7 = 0.54
let D7 = B7-B14
let E7 = C7-C14
let F7 = D7*E7
let G7 = D7^2
let H7 = E7^2
let I7 = I17*C7+I18
let A8 = A7+1
let B8 = 12.23
let C8 = 0.59
let D8 = B8-B14
let E8 = C8-C14
let F8 = D8*E8
let G8 = D8^2
let H8 = E8^2
let I8 = I17*C8+I18
let A9 = A8+1
let B9 = 14.43
let C9 = 0.67
let D9 = B9-B14
let E9 = C9-C14
let F9 = D9*E9
let G9 = D9^2
let H9 = E9^2
let I9 = I17*C9+I18
let A10 = A9+1
let B10 = 15.51
let C10 = 0.71
let D10 = B10-B14
let E10 = C10-C14
let F10 = D10*E10
let G10 = D10^2
let H10 = E10^2
let I10 = I17*C10+I18
let A11 = A10+1
let B11 = 17.09
let C11 = 0.8
let D11 = B11-B14
let E11 = C11-C14
let F11 = D11*E11
let G11 = D11^2
let H11 = E11^2
let I11 = I17*C11+I18
leftstring A13 = "Summen"
let B13 = @sum(B2:B11)
let C13 = @sum(C2:C11)
let D13 = @sum(D2:D11)
let E13 = @sum(E2:E11)
let F13 = @sum(F2:F11)
let G13 = @sum(G2:G11)
let H13 = @sum(H2:H11)
leftstring A14 = "Durchschnitte"
let B14 = @sum(B2:B11)/10
let C14 = @sum(C2:C11)/10
leftstring A17 = "Steigung k der Regressionsgeraden"
let I17 = G13/F13
leftstring A18 = "Achsenabschnitt F_0 der Regressionsgeraden"
let I18 = B14-A0*C14
leftstring A19 = "Empirische Korrelation"
let I19 = F13/@sqrt(G13*H13)
let J19 = F15/@sqrt(G15*H15)
leftstring A20 = "Bestimmtheitsmass R^2"
let I20 = @err^2
let J20 = @err^2
goto I0
