# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/hissingmicrophone

def main():
  word = input()
  if 'ss' in word.lower():
    print('hiss')
  else:
    print('no hiss')

if __name__ == "__main__":
  main()
