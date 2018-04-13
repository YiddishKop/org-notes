# Cat 2.1 Functions, epimorphism
## 2 way to design a language
every time you design a language, you have to provide the semantics for that language. Lot of language defined using so-called operational semantics, two way to define semantics:
1. operational semantics:
    - tell how things execute right, which define the operations of the language, eg. how one statement or expression transformed into another simpler one.

2. denotational semantics:
    - map things into some area you are intrested in, like mathematics. you build some mathematics model, and say "this statement or this construct corresponds to some mathematical thing."
    - like last course, for instance, type is a set of values.


## talk about PURE function
what is a pure function, it must can apply to all value of its argument's type. Not like partial function, it only suited for a subset of certain type of argument. 

### The Top level of Abstraction

but, how to describe the purity of a function?
> a function is pure if you can **memoise** it.

This means that you can turn it into a **lookup table**.

everytime you call this function once it's evaluated, you can remember it, the next time you can just lookup into a table.

so, types that are finite, only have finite number of elements, like Booleans, it's really easy to **tabulate**.

* functions on characters, they are really easy to tabulate.

* functions on Integers or Strings, they usually cannot be tabulated.

eg. 
``` scala
def isTrue(b: Boolean): Boolean = b == True
```
| input | output |
|-------|--------|
| true  | true   |
| false | true   |

> we must say that, the pure function is at the top level of abstraction, what we more concern is the bottom level of abstraction --- what is the atom(primitive thing), what are the simplest building blocks from which we can build more complex stuff

> First, we should **decompose** the problem, get to the little blocks at the bottom, and then **recompose** stuff from there

> when we are decomposing this idea of using procedures and types, we eventually get to the bottom and that's pure functions. So, on top of functions we can be building more complex stuff, including things like I/O. 

### The Bottom level of Abstraction
> keep in mind that, Programming can be modeled as a Cat of Set, which Set is an recursive concept --- one set can be element of another set.

what is a function
* function is some special relation(in mathematics)

what is a relation?
> keep in mind that, set is set of Cat, not set of Set Theory. set in Cat cannot see elments inside; set in Set Theory we can see inside.

    - relation is pairing 2 elment in 2 set, relation doesn't have to be symmetric. 

    - relation is just a subset of Cartesian product

![Cartesian product](https://i.imgur.com/ID3Jrer.jpg)

[[https://en.wikipedia.org/wiki/Cartesian_product?oldformat=true]]

relation which ilegal for function
![legal relation](https://i.imgur.com/N76JS0D.jpg)

**one** element of function CANNOT be mapped into a **bunch** of things.
![legal function](https://i.imgur.com/QcbYJ9U.jpg)

### Directionality of function
this is where directionality of function come from:
every element of start-set must have a mapping to element of target-set; but not requiring that for every element of target-set. which means that **we map a whole set to a subset of another set**.

![Whole to Sub](https://i.imgur.com/4J17S0m.jpg)

> Some terms:
> 1. Domain: Whole value of a start-set
> 2. f: the function
> 3. Codomain: Whole value of a target-set
> 4. Image: subset of Codomain,result of mapping Domain by f

![Terms of function](https://i.imgur.com/H1WPR6M.jpg)


**Directionality and Mapping** are so important concept, that it will occur many times in this course:
1. function: mapping between 2 set(objecst)
2. Functor: mapping between 2 Cat
3. Natural transformation: mapping between 2 Functor

All these mappings have the same kind of directionality.


#### isomorphism and inverse
> How to define inverse of a given function
``` haskell
f :: a -> b
g :: b -> a
g * f = id_a
f * g = id_b
```
> what is isomorphism?
function that is invertible is called **isomorphism**
**g * f = id_a ; f * g = id_b**
we can say: 
**f is isomorphism if existing a g to make 2 equation available
**

> tips: you see that, we never look inside of a set, we just use and ONLY use function to define what is isomorphism

when we define something ONLY by function(arrow), we get an general definition for any Cat, not only for some Cat but **for all Cat** .

but when we use **inside view** of set, we trap ourself to details, which impose restriction on availabe range of this definition.

isomorphism is excellent:
isomorphism build a one-to-one relatioship between 2 set
isomorphism kinda tell you that these 2 things are for **some intents and purposes identical**

for finite 2 set: one-to-one
for infinite 2 set: because of infinite things become more complex

```
Even Nature Number <-------------> Natural Number
y = 2x
```

#### 2 reason function always not isomorphism
1. function will collapse elements of a set( because function allow many-to-one mapping)
2. image is always a subset of Codomain
   - then if you inverse f, maybe we call it g. But for g, his input should be the whole codomain
   - then this is something like: f :: Int -> Double, g :: subDouble -> Int
   - then we CANNOT compose them. 
   - so you can think of function like a time related process
   - you can boil an egg; you CAN NOT unboil an egg
   
#### abstraction vs. model
##### abstraction
from another point of view, we don't hope function to be invertible . Because we don't want to care about the inside of the set, we don't want to trap ourself to details, details is not abstractive.   

##### model
but when refering to practical things, we should use **model**.we should do some mapping, that from 3-d person to 2-d shadow.

In mathematics, if a function **dose not collapse** things, we call it **injective function**.  And if image equals to Codomain, we call ti **surjective function**.

* collapse: 3-d person to 2-d shadow (many-to-one)
* injective: 3-d person without a hat to 3-d wax figure with a hat (one-to-one)
* surjective: 3-d person without a hat to 2-d shadow without a hat

or we can say:
* injective：**一对一**，不坍缩，有漏 or 无漏
* surjective: 多对一 or 一对一，坍缩，**无漏**

![injective vs. surjective](https://i.imgur.com/DCYg1ih.jpg)

isomorphism = injective + surjective

#### come back to abstraction
what we talk about above in section 'model' is too detail:
* one-to-one --- element related
* image equals Codomain --- element related

But, as we said before, we don't like detail, we are talking about Cat.

**can we describe clearly what is "injective" and "surjective" ONLY by morphism(arrow/function), if we can not see the elememnts**

YES, we can, but it's a little tricky, because I have to talk about **all the other** objects in the category, all of them, in order to define this one property.

this is very characteristic point in Cat.

when you define a property of an object or an arrow, you define it with respect to essentially everything else. you can not just focus on one litte thing, because no matter how good your microscope is you cannot look inside this litter point.

| Set Theory | Category Theory      |
|------------|----------------------|
| injective  | monic - monomorphism |
| surjective | epic - epimorphism   |


#### define epimorphism
**How**
>first from a set, then we define a surjective function that can be expressed purely in terms of other functions.

**what is not epimorphism**
>exist some point outside of **image** but inside of Codomain.

**build a new set and build functions to compose original function**
>f :: a->b
>build 2 new functions: g1 and g2
>g1 :: b->c
>g2 :: b->c

![a new set c and new functions g1,g2](https://i.imgur.com/f67TF7I.jpg)

**prove by contradiction**
>if f is not surjective, we can not infer from:
>`g1 * f = g2 * f`
>to:
>`g1 = g2`
> 
>for all set c, for any g1 and g2, 
>if g1 * f = g2 * f => g1 = g2
>then f is a epimorphism function in Cat

Although, we only build ONE new set, but if take it to any other Set, this epimorhpism will also avaiable.

all above proving process, is so Cat manner:
if you want define some property, you must take the WHOLE university( for all set c, for any g1 and g2 ) into account. Or we might say, if you want build some law, all people of the university must allow you to do, then you can do it. 

we also must notice that:
**what we use to define a epimorphism is just use and ONLY use function composition** ,yes we did it. we just define something ONLY using arrows.

remember that, function is arrow from one set to another set, nothing related to details --- the elements inside the set. So, **by using and ONLY using function**, we **keep the abstraction** of the Cat, this is what we want the **abstraction**

#### why epimorphism is important
because:
if f is epimorphism, then we can use it like GCD of production
```
3 * 2 = 3 * 2
=> 3 = 3
```
g1 * f = g2 * f
if f is epimorphism =>
g1 = g2

#### 6 kinds of morphism
1. 同构（isomorphism）
    - 令f:X→Y为一个态射。若存在态射g:Y→X使得  和  成立，则f称为一个同构。g称为f的逆态射，逆态射g如果存在就是唯一的，而且显而易见g也是一个同构，其逆为f。两个对象之间有一个同构，那么这两个对象称为同构的或者等价的。同构是范畴论中态射的最重要种类。
2. 满同态（epimorphism）
    - 一个态射f:X→Y称为一个满同态，如果对于所有Y→Z的态射g1成立。这也称为epi或epic.具体范畴中的满同态通常是满射（surjective）函数，虽然并不总是这样。 
3. 单同态（monomorphism）
    - 态射f:X→Y称为单同态，如果对于所有Z→X的态射g1，g2， 成立。它也称为mono或者monic.具体范畴中的单同态通常为单射（injective）函数。
4. 双同态（bimorphism）
    - 若f既是满同态也是单同态，则称f为双同态（bimorphism）。注意每个同构都是双同态，但不是每个双同态都是同构。例如，交换环的范畴中，包含映射Z → Q是一个双同态，但不是一个同构。如果在一个范畴中每个双同态都是同构，则这个范畴称为一个平衡范畴。例如，集合是一个平衡范畴。
5. 自同态（endomorphism）
    - 任何态射f:X→X称为X上的一个自同态。
6. 自同构（automorphism）
    - 若一个自同态也是同构的，那么称之为自同构。
7. 若f:X→Y和g:Y→X满足  可是证明f是满的而g是单的，而且  :X→X是幂等的。这种情况下，f和g称为分割（split）.f称为g的收缩（retraction）而g称为f的截面。任何既是满同态又是分割单同态的态射，或者既是单同态又是分割满同态的态射必须是同构。





# Cat 2.2 Monomorphisms, simple types
the same process with proving epimorphism:

1. what is not a injective
![many-to-one is not injective](https://i.imgur.com/TweE1Yf.jpg)

2. how can we describe it using other function, rather than looking inside the elements.

we use **pre**-**composition** other than post-composition(used in defining epimorphism)

![define monomorphism](https://i.imgur.com/oI3vOMS.jpg)

```
for all set c, any g1 g2:
if : f * g1 = f * g2 => g1 = g2
then : f is monomorphism
```

epimorphism vs. monomorphism

| epimorphism          | monomorphism         |
|----------------------|----------------------|
| * surjective(full)   | * injective(1:1)     |
| * post-composition   | * pre-composition    |
| * g1*f=g2*f => g1=g2 | * f*g1=f*g2 => g1=g2 |

## epimorphism and monomorphism
we know that:
> isomorphism = injective + surjective

but for Cat:
> isomorphism != epimorphsim + monomorphism

## Talk more about set
because set is what used to model type(object), we shoud take deep understand it.

### 0 element set
**So, what is the simplest set**
> empty set is the simplest set

**Dose empty set has related type in programming language**
> you will not find an empty set in any imperative language. But you can find it in Haskell, but I must say type in Hasekll have bottom member, so that the empty set is not empty, it does have a bottom member. But if you just ignore the infinite loop of executing, then the empty set is the correct type called `Void` , no construct inside it.

**Is there f::Void -> Int ?**
> In mathematcis, yes. it is excellent, because we can now have a identity function:
``` haskell
f :: Void -> Int
id_void :: Void -> Void
```

> this is a good function, but you can never call it, but it's sure exist.

**Void is false in logic, you can not prove it, you can not prove false. and in type theory, function is something to do proving.**

### 1 elements set

**Singleton set : Unit**
``` Haskell
Unit :: a -> ()
one :: () -> Int
two :: () -> Int
```
for () is the type of Singleton set, so it only have one elment. so if it's taken as type of argument, then this function must always return the same value. 

then you will find a truth:
if the output set have 2 elments, like Boolean. Then function of this form `fn :: ()->Boolean` only have 2 different function.

because in this situation, thers is no many-to-one mapping, there is ONLY one-to-one mapping. So, the number of elements in output set decide the number of mappings, do that decide the number of functions.

**A big BONG~~~**
then you will find that, we may **use and ONLY use** function to compute the number of elements in output set

Function from a single set to any other set, they define in a way, the elements in a set.

<<From elements to morphism(function/arrow)>>
So we begin to discuss morphisms from this special set(Unit) instead of elements.

### 2 elements set

We further learn that boolean is not as atomic structure in our cagetory of set. In general, it can be defined as the sum of two unit types. this type is not so independent.

but 0 and 1 element set (or type.), they form the basis for all others.

A function that returns a Boolean type, called **predikatom**.
