import concurrent.futures


NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def prime_filter(num):
   if num > 2:
      for i in range(2, num):
         if num % i == 0:
            return False
   return True



if __name__ == '__main__':

   with concurrent.futures.ThreadPoolExecutor() as executor:
      futures = []
      for num in NUMBERS:
         futures.append(executor.submit(prime_filter, num))
      for future in concurrent.futures.as_completed(futures):
         print(future.result())
