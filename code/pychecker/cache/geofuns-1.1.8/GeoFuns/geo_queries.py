query = '''
WITH x AS (
SELECT
  PERCENTILE_DISC(offer.preisProQm, 0.5) OVER(PARTITION BY geo.koordinaten) as med_price,
  count(offer.preisproqm) over(partition by geo.koordinaten) as counts,
  geo.koordinaten as coords,
  geo.wohnquartierskennziffer as kz,
  ROW_NUMBER() OVER(PARTITION BY geo.wohnquartierskennziffer ORDER BY geo.wohnquartierskennziffer) as name
FROM
  offerData.offerData as offer
JOIN
  geoData.nexigaWohnquartiereGeoData as geo
  ON ST_CONTAINS(ST_GEOGFROMTEXT(geo.koordinaten),ST_GEOGPOINT(CAST(offer.latitude AS FLOAT64),CAST(offer.longitude AS FLOAT64)))
WHERE
  offer.ort = '{}'
GROUP BY
  geo.koordinaten, geo.wohnquartiersKennziffer, offer.preisProQm
)
SELECT
  x.kz,
  med_price,
  coords,
  avg(s22.kaufkraftJeEinwohnerInEuro) as kaufkraft,
  1 - COALESCE((avg(s22.arbeitsloseInsgesamt) - min(s22.arbeitsloseInsgesamt))  / NULLIF((max(s22.arbeitsloseInsgesamt) - min(s22.arbeitsloseInsgesamt)),0), 0) as employed
FROM x
JOIN
  (
    SELECT
      wohnquartierskennziffer,kaufkraftJeEinwohnerInEuro,  einpendler, auspendler, arbeitsloseInsgesamt, fortzuegeIngesamtEinwohner, zuzuegeInsgesamtEinwohner, einwohnerinsgesamt
    FROM
      socialdemographicData.nexigaKgs22Data2019
    UNION ALL
    SELECT
      wohnquartierskennziffer,kaufkraftJeEinwohnerInEuro, einpendler, auspendler, arbeitsloseInsgesamt, fortzuegeIngesamtEinwohner, zuzuegeInsgesamtEinwohner, einwohnerinsgesamt
    FROM
      socialdemographicData.nexigaKgs22Data2015
    UNION ALL
    SELECT
      wohnquartierskennziffer, kaufkraftJeEinwohnerInEuro, einpendler, auspendler, arbeitsloseInsgesamt, fortzuegeIngesamtEinwohner, einwohnerinsgesamt, zuzuegeInsgesamtEinwohner
    FROM
      socialdemographicData.nexigaKgs22Data2016
    UNION ALL
    SELECT
      wohnquartierskennziffer, kaufkraftJeEinwohnerInEuro,einpendler, auspendler, arbeitsloseInsgesamt, fortzuegeIngesamtEinwohner, zuzuegeInsgesamtEinwohner, einwohnerinsgesamt
    FROM
      socialdemographicData.nexigaKgs22Data2017
    UNION ALL
    SELECT
      wohnquartierskennziffer, kaufkraftJeEinwohnerInEuro, einpendler, auspendler, arbeitsloseInsgesamt, fortzuegeIngesamtEinwohner, zuzuegeInsgesamtEinwohner, einwohnerinsgesamt
    FROM
      socialdemographicData.nexigaKgs22Data2018
    ) s22 ON s22.wohnquartierskennziffer = x.kz
    JOIN
    (
    SELECT 
      wohnquartierskennziffer, passantenfrequenzscore
    FROM
      socialdemographicData.nexigaKgs36Data2019
    UNION ALL
    SELECT
      wohnquartierskennziffer, passantenfrequenzscore
    FROM
      socialdemographicData.nexigaKgs36Data2015
    UNION ALL
    SELECT
      wohnquartierskennziffer, passantenfrequenzscore
    FROM
      socialdemographicData.nexigaKgs36Data2016
    UNION ALL
    SELECT
      wohnquartierskennziffer, passantenfrequenzscore kaufkraftJeEinwohnerInEuro
    FROM
      socialdemographicData.nexigaKgs36Data2017
    UNION ALL
    SELECT
      wohnquartierskennziffer, passantenfrequenzscore
    FROM
      socialdemographicData.nexigaKgs36Data2018
    ) s36 ON s36.wohnquartierskennziffer = x.kz
    JOIN
      socialdemographicData.nexigaKgs44Data2019 as s44
    ON s44.wohnquartierskennziffer = x.kz

  WHERE name = 1
  GROUP BY
  x.kz,
  med_price,
  coords
'''
