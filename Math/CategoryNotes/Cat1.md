# Cat 1.1 --- philosophical introduction to Cat
Cat in chinese is 范畴论

in math or phisical area, something CAN NOT be divided, something CAN NOT be composable.

In Cat, we talk about the human brain --- which good in dividing and composing.

Cat is more about the epistemology than ontology (范畴论是一门认识论多于本体论的科学)

* epistemology is about reasoning, about leaning some stuff.
* ontology is about what things are.

May be we can not learn what things are, but we can learn how we can study, and that is what Cat tell us.

# Cat 1.2 --- what is a category

1. Abstraction
    - we want to get rid of the **details**, things are different because the **detail**
    - if no **detail**, they suddenly become **identical**.
2. Composition
3. Identity
    - things become identical because of abstraction
    - "really same" or "not really same, but we'll look at itas if it were the same" --- this is what **Homotopy type theroy**,which is hot now
    - equal, isomorphism

**(2)(3) defined the whole things about Cat**


## so what is category

### Elements of Category
> category is a **bunch** of objects

1. category
2. objects
    - what is an obj, you CAN NOT tell.
    - because object in this Cat is a **primitive** concept. 
    - has no properties; has no internal structure
    - it like an atom, a point.
    - the reason Cat have objects, is to mark the begining and end of an **arrow**
    - don't server any other purpose
3. morphism(arrow)
    - something goes between 2 objects
    - also **primitive** concept.
    - has no properties; has no internal structure
    - but have begining and end
    - [0, infinite] arrows between 2 objects
    

> when we talk about arrow, it is very like the hunter-gather in ancient time.

hunter-gather knows **spatial**.

> In a mathmatical course, professor often draw some point on backboard, and they also have **spatial realationship**: above/below/left/right.

> Cat, object, also have **spatial relationship** , higher level of abstraction, lower level of abstraction.

hunter-gather knows **movement**.

> Cat, arrow, has start point and end point, which is something like **movement** and **relationship**


everytime you define a Cat, you specify what are the objects of ths Cat, and for each pair of objects you specify the arrows that between them.

![arrows between object is in an arbitray manner](https://i.imgur.com/ADGn36k.jpg)

you can have very arbitray manner of combination of arrows and objects:
1. [0, infinite] arrows from objects to itself
2. [0, infinite] arrows from this to that
3. [0, infinite] arrows from that to this

> tip: arrows can have different name, so, many arrows with same geginning and ending can have different name, they are differnet.




### Compostition
![composition](https://i.imgur.com/8tJGa6N.jpg)

gºf --- "g after f"
which also illustrate the order of computation, computation of g come after computation of f

maybe, there are other composition of these two objects, but this "g after f" must exist.

if composable then there must be a composition.

what you need to describe a Cat, is a composition table, like a multiplication table, from which you can compute out many many numbers, Cat is some things "the whole objects computed form composition table, every composition is a arrow"


### Identity
**Axiom1 : Identity**
> every object has an circle arrow, this arrow is called **Identity** --- notation:'id_a'(if the object is called 'a').

why name it 'identity', because in an composition, it just play an role like "do nothing". Same with what `1` do in an production, like `3 * 1 = 3`, where `1` is the **identity**

**Axiom2 : Left/Right Identity**
> id_aºf = f
fºid_a = f

![Identity](https://i.imgur.com/YhDSFtC.jpg)



**Axiom3 : Association**
> hº(gºf) = (hºg)ºf

![Association Rule](https://i.imgur.com/oiPOw7H.jpg)

we must say that, axiom-3 maybe not "equal" but just "isomophic"

> tip: keep in mind that, if some thing is a Cat, he must obey this 3 axiom, vice and versa.


#### why Cat is not a Set
set is just something just what it looks like.
```
{1,2,3} 
// this is a set, has nothing implicit information.
// it has 3 elements: 1, 2, 3
```
Cat is something far more than what it looks like.
```
Cat{1,2,3}
// if no arrows in it, it is truely a set
// but if arrows appear, it exponentially grow like a production
// table.
```

#### isomophims and identity
isomophism is a **weak** identity.




## One example of programming
| Cat    | Prog     |
|--------|----------|
| object | type     |
| arrow  | function |

### arrow(or morphism) is a function between two types.

> Cat will be more complex in Haskell, because Haskell is a **lazy language**, type will contains this undefined value, the **bottom value**, this means if you try to evaluate it you will get into an infinite loop.

> Cat rarely concern about **time**, because **time** is hard to describe in math, but for programming, ensentially it's a calculation, time is very important, infinite loop is meaningless in that scenario.

> So in Haskell, codes trap into a infinite loop will return an Integer --- bottom value which menas it never terminate.

### type is just a **set of values**

the simplest model for **types** is that they are just **sets**(not suited for Haskell, because of bottom value, but suit for ML)

then, we can model programming as **in a Cat of sets**

functions are just functions between sets.

function from one set to another set.

| Cat    | Prog     | ModelProg             |
|--------|----------|-----------------------|
| object | type     | set of values         |
| arrow  | function | function between sets |

![model programming](https://i.imgur.com/i7XrRPy.jpg)

## schizophrenic view of Cat
a lot of Cats come from some model:

eg. you take set as object of Cat, but object in Cat theory is a primitive thing, it has no internal structure,no properties. But set has, it has structure, it has elements in it.

And, arrows in this scenario will also change, it is a mapping from elements to elements.

But, when we build a Cat from this model, we must forget about all things above.

> I get blind, and I say "this is a set", what's inside of the set? I have no idea, it's an atom, it has no structure, because I'm putting on my Category glasses.

> when refer to arrow between sets, I get blind again. I just know set A is an object, set B is an object, I have 10 arrows maybe between A and B. "But, what are these arrow？", I don't know.

**At this time, what about the Identity arrow**?

In this model, identity arrow, is only the arrows that starting from **elment** and end at it self. Don't count in the arrows start from and end at the same set, but with different elements, they are not **Identity**.

**why**

because **Identity** is only according with **Composition**, who can hold the orginal state like nothing happens, will be the **Identity arrow(function)**

![Identity in set model](https://i.imgur.com/dWxBz88.jpg)

## why we need this blind view of Cat
because, ONLY in this way, we can talk about a lot of meaning things, like we can infer the follow things ONLY by arrow(morphism):
1. which set is empty
    - although we "forget" about all things in set, but we can infer wheather this set is empty by morphism, ONLY by morphism, nothing else.
2. which set has sole element


Or we can say, you really can get many information from just the muliplication table, you don't really have to know what's inside these sets.

> And that gives you a completely new way of looking at things, a more abstract way of looking at things.

> when you thinking about what's inside of set, you're just thinking like "assembly language", Cat gives you higher level language, you just look at how they are connected with arrows.

> This is the ultimate goal of encapsulation, you have an object, it's a data type, it's a set, but you cannot look inside of it. It shrunk to a point, All you have is its interface, its interface is how it connects to other objects. The arrows coming out of and into this object, they defined the Interface.
