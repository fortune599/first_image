def main():
  f = open("image.ppm", "w+")
  f.write("P3 500 500 255\n")
  for y in range(500):
    for x in range (500):
      if (y-15 < -1.0/256 * (x-250)**2 + 270 < y-1 and (150 < x < 230 or 270 < x < 350) and y < 275):
        r = 0
        g = 0
        b = 0
      elif ((x-200)**2 + (y-275)**2 <= 100 or (x-300)**2 + (y-275)**2 <= 100):
        r = 0
        g = 0
        b = 0
      elif ((x-250)**2/32**2 + (y-325)**2/8**2 <= 1):
        r = 0
        g = 0
        b = 0
      elif ((x-250)**2 + (y-250)**2 <= 16384):
        r = 255
        g = (y-122) % 256
        b = 0
      else:
        r = 0
        g = 0
        b = 0
      f.write("%d %d %d\n" % (r,g,b,))
  f.close()
  print("image.ppm created")
  return



if __name__ == "__main__":
  main()
