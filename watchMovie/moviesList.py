import argparse
parser = argparse.ArgumentParser()


parser.add_argument("-a", "--addMovie", dest = "add", help="add Movie")
parser.add_argument("-e", "--editMovie", dest = "edit", help="edit Movie")
parser.add_argument("-rm", "--removeMovie", dest = "remove", help="-remove Movie")
parser.add_argument("-w", "--watched", dest = "watched", help="watched Movie")

args = parser.parse_args()

##destination ( dest = "add") to function
#def add()
#sdef edit()
#sdef remove()
#sdef watched()