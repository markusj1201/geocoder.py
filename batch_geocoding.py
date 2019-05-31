import geocoder
g + geocoder.mapquest([Midland, TX', Denver, CO'], method='batch')
for result in g:
  print(result.address, result.latlng)
  
 ('Midland', [31.9973, -102.0779])
 ('Denver', [39.7392, -104.9903])
