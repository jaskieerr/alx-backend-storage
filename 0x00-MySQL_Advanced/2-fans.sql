-- Black Viel Brides

SELECT origin, SUM(FANS) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
