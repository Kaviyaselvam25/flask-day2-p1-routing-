from flask import Flask
app=Flask(__name__)
@app.route('/')
def project():
    return "<h1 style='color:blue'><center>My first routing page</center></h1><hr><h2 style='color:red'><center>The Tortoise And The Bird</center></h2><p> A tortoise was resting under a tree. On this tree, a bird had built its nest. The tortoise mocked the bird for having a home built with broken twigs, which it had to build itself. He bragged about his own shell and said the bird must be jealous. The bird told the tortoise that its nest might be shabby, but it had space for its friends and family. At the same time, the tortoise’s shell could never accommodate anyone else except the tortoise himself.<br><br><br><strong>Moral:</strong><br> A crowded hut is better than a lonely mansion.</p>"

@app.route('/abc')
def project1():
    return "<h1 style='color: brown'><center>My second page</center></h1><hr><h2 style='color:plum'><center>The Stork and the Crab</center></h2><p>There once was an old stork who could not catch fish anymore. As he grew hungrier, he devised a plan. He told the fish in the tank that the farmers would soon empty out the tank and grow crops there. He offered to take the distressed fish to a bigger tank further away. The fish happily agreed, but the stork would take them to a rock and kill them. There was also a crab in the tank who wished to be saved. The stork, thinking he could try some new food, agreed to take him. However, the crab quickly noticed the fish bones on the rock. He immediately dug his claws into the stork’s neck and killed him. He then went back to the old tank and informed the other fish.<br><br><br><strong>Moral:</strong><br> A sharp mind is your greatest strength.</p>"

if __name__=='__main__':
    app.run(debug=True)

