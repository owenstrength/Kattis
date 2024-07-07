# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/different

from sys import stdin

def main():
  for line in stdin.readlines():
    a,b = map(int, line.split())
    print(abs(a - b))

if __name__ == "__main__":
  main()
