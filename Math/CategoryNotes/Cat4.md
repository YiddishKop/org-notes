<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Cat 4.1 Terminal and initial objects](#cat-41-terminal-and-initial-objects)
    - [More about Kleisili Category](#more-about-kleisili-category)
    - [Once more, Set and Category](#once-more-set-and-category)
        - [Universal Construction Method](#universal-construction-method)
        - [Singleton Set: ONE arrow point to it from ANY](#singleton-set-one-arrow-point-to-it-from-any)
            - [Terminal object: all arrow convergeo on](#terminal-object-all-arrow-convergeo-on)
        - [Two elements Set: TWO arrows point to it from ANY](#two-elements-set-two-arrows-point-to-it-from-any)
        - [Empty Set: ONE arrow point to Any from it.](#empty-set-one-arrow-point-to-any-from-it)
            - [Initial object: all arrow emit from](#initial-object-all-arrow-emit-from)
        - [More about Terminal object and Initial object](#more-about-terminal-object-and-initial-object)
        - [How many Terminal object, and Inital object](#how-many-terminal-object-and-inital-object)
        - [Ranking of Googling](#ranking-of-googling)
            - [the simplest pattern: One object pattern](#the-simplest-pattern-one-object-pattern)
- [Cat 4.2 Products](#cat-42-products)
    - [one more thing about the outgoing arrow from an terminal object](#one-more-thing-about-the-outgoing-arrow-from-an-terminal-object)
    - [Cartesian Product expressed by Category](#cartesian-product-expressed-by-category)
        - [appetizer 1](#appetizer-1)
        - [appetizer 2](#appetizer-2)
        - [Dining](#dining)

<!-- markdown-toc end -->

# Cat 4.1 Terminal and initial objects

## More about Kleisili Category


as we say in last lecture:
Kleisili Cat has **same objects** but **different arrows** with original Cat from which we build our Kleisli Cat.

but, `a ---> (b,String)` is just an arrow with end object like a new type --- a pair(or tuple). 

So, it looks more like "different objects", isn't it?

Let's say that:
1. we have a functor(map) : **a --> (a,String)**, we call `(a,String)` **ma**
2. If there is an arrow: `a --> mb` in original Category, then it becomes an arrow `a --> b` in Kleisli Category

I'm constructing this in such a way that taking the arrow `a --> mb` from original Category, so it's my embellished arrow, so to speak. And the **embellished arrow** in original Cat is a **direct arrow** in the Kleisli Cat

**Definition and Implemented**
![building Kleisili Category from orginigal Category](https://i.imgur.com/f1RfNDn.jpg)

It's like that, Klesili category on the right is definition, the original Category on the left is the implementation of it:
1. Kleisli get objects, original implement the objects(by just use the same objects)
2. Kleisli need the same connection with original, the original gives how to do mapping.

you must know that, many times, we dont know how to do this mapping a --> ma, so that we can do composition, but once we can like this time:
1. find the mapping: for axiom1
2. find how to compose: for axiom2,3

| Kleisli Cat                          | original Cat                              |
|--------------------------------------|-------------------------------------------|
| identity: a->a                       | a ->(a, "")                               |
| composable: a->c = a->b,b->c         | a ->(c, String)= // a triky way see below |
| associativity: (a->b)->c = a->(b->c) | tricky way see below                      |

``` scala
def compose[A,B,C](fn1: A=>(B,String), fn2: B=>(C,String):A=>(C,String) = {
  (a:A) => {
    val p1 = fn1(a)
    val p2 = fn2(p1._1)
    (p2._1, p1._2 + p2._2)
  }
}

```
if we can find this tricky way ,we then can build a category(called Kleisli) from another Category

So, with the restriction of same objects and same connection between objects, if original can find:
1. the mapping from a to ma, and apply it to every object.
2. by this mapping, can prove the Kleisli arrows is a Category.

then, done! we build a new Category whose component and evidence of tobe a Category all given by a nother Category.

[Kleisli in scalaz](http://eed3si9n.com/learning-scalaz/Composing+monadic+functions.html)

### why we need Kleisli arrow or Kleisli category ###
because of composition, we want to provide some uniform interface to combine different categories which can mapping to the same Kleisli category.

| original category1 | original category2 | original category3 | Kleisli |
| a->m1b             | a->m2b             | a->m3b             | a->b    |


## Once more, Set and Category
by now, what can we say about the relation between set and cat.

Set:
* we can deep in details --- elements in set
* by elements, we can find functions between elements
* functins apply on elements can compose

Cat:
* we can't see elements, we ONLY see arrows;
* while arrows come from the the function between sets in Set theory
* one function between sets in Set theory; one arrow in Set Category(set - set of values - type of values - object in category)
* arrow combine together, gives you 3rd arrow

Questions:
1. but, what is empty set, how do define it in Set Category?
2. but, what is singleton set, how do define it in Set Category?
3. but, what is Cartesian Product of 2 sets, how do define it in Set Category?
4. ...

**all these stuff should completely redefined, use and ONLY use arrows(functions)**

we do have a method.

### Universal Construction Method
It has no way to look inside the 'universe', but remains ONLY to determine the properties of the object, based on the relationship of the object with others, these "relation"( a term we used to see many many times) with other objects is arrows. 

When we think about the object and relation, we need to define it in **relation to all other objects of category**, just like to think about the entire universe of objects.

Like what we have talked about before: Epimorphism and Monomorphism, they were all determined with the help of the universe.

And now, we'll do similar things, using Universal Construction method. A general method of Universal Construction is similar to use the search engine(google something):
1. you define a **pattern**: a pattern is some combination of objects and arrows, and could be very simple pattern like ONE object or ONE arrow.
2. then, **Googling** with this pattern, it will show all results in this Category
3. you **may get infinite result** from Category, because this pattern may be very popular pattern in this Category, this is not good enough.
4. so, you want to **rank**, just like google dose. if you have 2 hits for the same pattern, you need to choose which is better.
5. but if they are **not comparable**, eg. partial order and pre-order
6. so maybe some objects can't compare, but some others still can compare. If you have the top of the ranking, you determine the object that you're looking for.

### Singleton Set: ONE arrow point to it from ANY
Any other object if seen as One object, then this object has and has ONLY one arrow point to Unit,like a function with one augument, but function will just ignore this augument and println or return nothing than a ():

![any to singleton set](https://i.imgur.com/QrFpE6y.jpg)

``` scala
def fn(a: Any):Unit = println("hello")
```
``` scala
scala> ().getClass
res1: Class[Unit] = void
scala> (println("")).getClass
res2: Class[Unit] = void
```
> **Unit**(which means singleton set here) is something represented by two types in scala: one for AnyVal --- **Unit**,has one instance: **()**; the other for AnyRef --- **Null**, has one istance **null**.

> void(which menas empty set here) is something represented by Nothing in scala, Nothing has several derived types: Option[Nothing] = None; List[Nothing] = Nil...

#### Terminal object: all arrow convergeo on
So we can say, **Singleton Set as an object**, is the Terminal object, because he is the terminal for all arrows, all the **arrows converge on it**.

> Math definition:
>(1) for any type a, exist f :: a->()
>(2) for any type a, if exist two functions f::a->() g::a->(), then f = g

**Not every object has Terminal object**:
if relation is <=, then in Natural Number, there is no biggest number; So, there is No terminal object.
### Two elements Set: TWO arrows point to it from ANY
2 elements Set such as Boolean, will have 2 functions from any other objects to Boolean: one point to element true; the other point to element false:
``` scala
def (a:Any):Boolean = true
def (a:Any):Boolean = false
```
### Empty Set: ONE arrow point to Any from it.
**No function: Any => Nothing.**
There are no functions from any other sets to Empty set, because functions must have some terms to describe like "from xx elemets to xx element", elment-to-element, so once no elments then no function.

**Have function: Nothing => Any.**
why? it's something like function without argument:
```scala
def fn = 3
def fn = true
def fn = List(1,2,3)
```
#### Initial object: all arrow emit from

![empty set to any](https://i.imgur.com/EjM3i9P.jpg)

> Math definition versa to terminal object:
>(1) for any type a, exist f :: ()->a
>(2) for any type a, if exist two functions f::()-> a, g::()->a, then f = g


### More about Terminal object and Initial object
Not every Category has an initial or terminal object, if it has both them, itwill look like:

![every complex path will lead to the same short directly path to terminal object](https://i.imgur.com/2BzvrZW.jpg)

any path (function composition) to terminal object will shrunk to a single unique arrow.

any path (function composition) to 2-elements object will shrunk to two arrows, one for true, another for false.

the same with Initial object, if we reverse the arrow.


### How many Terminal object, and Inital object
or we ask a step more:
how do you think about object equality.

In fact, we have the arrow equality formula:
> if g*f = h*f => g = h

but we never define object equality, so really this is a forbidden question that we can not define.

But instead we have another weapon: **isomorphic**

> It turns out that terminal object is unique up to isomorphism.

> If you have 2 objects that satisfy the conditions of the Terminal object, then they are isomorphic.

> tips, before this lecture, we defined the isomorphism of arrows; now we define the isomorphism of objects.

| isomorphism of arrow             | isomorphic of objects      |
|----------------------------------|----------------------------|
| if f:: a->b, then exist g:: b->a | if there is a isomorphism  |
| g*f = id_a                       | between two objects, these |
| f*g = id_b                       | two objects are isomorphic |
| f,g isomorphism or invertible    |                            |

**the conditon is even stronger: this isomorphism between them is unique.**

Some example whose isomorphism is not Unique:
2-elements set to 2-elements set

|               | black/white | true/false |
|---------------|-------------|------------|
| isomorphism 1 | balck       | true       |
|               | white       | false      |
|---------------|-------------|------------|
| isomorphism 2 | balck       | false      |
|               | white       | true       |

number of isomorphism, means that how many ways you can find the 1-to-1 relationship between all the values of one type and another 

Prove again about the isomorphism 

![terminal object a and b](https://i.imgur.com/ZD9pAXR.jpg)

eg: a,b both terminal object here, then
```
g:: b -> a
f:: a -> b
g * f = h
h:: a -> a
```
but because as we say before, Any object(include terminal object itself) has and has ONLY one arrow to terminal object, so according to axiom-1 of Cat, so we can infer:
```
h = id_a
```
because a it self is in "every object of category", so it must have and ONLY have one arrow to itself.

for other object, who is not the terminal object, we can ONLY infer `h` is a function from a to a, but we can not infer `h` equals to `id_a`.

### Ranking of Googling

remeber the analogy Universal Construction method to search engine

> And now, we'll do similar things, using Universal Construction method. A general method of Universal Construction is similar to use the search engine(google something):
> 1. you define a **pattern**: a pattern is some combination of objects and arrows, and could be very simple pattern like ONE object or ONE arrow.               
> 2. then, **Googling** with this pattern, it will show all results in this Category
> 3. you **may get infinite result** from Category, because this pattern may be very popular pattern in this Category, this is not good enough.
> 4. so, you want to **rank**, just like google dose. if you have 2 hits for the same pattern, you need to choose which is better.
> 5. but if they are **not comparable**, eg. partial order and pre-order
> 6. so maybe some objects can't compare, but some others may compare. but if you have the top of the ranking, you determine the object that you're looking for.

#### the simplest pattern: One object pattern

![one object pattern and terminal is best of all hits](https://i.imgur.com/4PQvgLu.jpg)

one object pattern will match all objects in this Category, this is not what we want ,so we need to rank them.

Now, we shoud sepcify **how** to do **Ranking**?

> we said that, a better than b, if there is a unique arrow form b -> a.

but you may ask:
* what if there are 2 or more arrows between any 2 objects?
* why we need "uniquness"? why many?

for 1st question, then we can not compare them, so simple answer, then we can not find the top one of this pattern.
for 2nd question, just recall total/partial/pre order, if the relation of 2 object is order(like bigger or smaller), we need the relation tobe sole, we need it tobe exclusive.
because we don't want `a > b` meanwhile `b > a`, for **ranking** it's actually the same scenaio.

after that, we can say the best is the 

**terminal object who has the largest number of input arrow**.

by reverse this operatioan, we can say the worest is the 

**Initial object who has the largest number of outpu arrow**.

then we can find who is the best match according to our patttern: one object pattern


# Cat 4.2 Products

## one more thing about the outgoing arrow from an terminal object
There truely are some outgoing arrow from a terminal object,and they are very important, because:

> Every arrow from a terminal object to another object is a definition of a **generalized element** in this other object.
 
``` scala
// 'unti' => Int
scala> def fn():Int = 3
fn: ()Int
// 'void' => Int
scala> def fn:Int = 2
fn: Int
```
> 2 lines of code above, are different, 1st is from `unit`(Unit or Null in scala) to Integer, 2nd is from `void`(Nothing in scala) to Integer


"generalized elment" is what happend in a set, when you map a singleton set into some other set.That's equivalent of **picking** one element and saying this element of the singleton set is mapped into this particular element of the other set.

There are many morphisms each of them takes a different elment.

![picking element of the target set](https://i.imgur.com/IxzsAq2.jpg)

This is why it's important, because like if you want to have a category that sort of is like Set Category, there is a bunch of category that have similar properties as the category of sets, so there are certain things that you would like to have in them and one of these things is being able to having a terminal object because the teminal object gives you this way of picking elements.


> Actually, in Category theory, when you have one thing, you can freely have another thing, just by reversing.

When you have a terminal object, you just reverse the direction of arrow, you get everything of terminal object in initial object.


you always can get a opposite category, which have the totally reversal direction arrows with other things keeping same.

![Opposite Category](https://i.imgur.com/BUsgvFe.jpg)

prove opposite cat is a cat:

tip: when you reverse the arrows, you always need to reversing the order of composition too.

![composition of Opposite Category](https://i.imgur.com/f1RfNDn.jpg)

Initial object is the Terminal object in its Opposite Category.

## Cartesian Product expressed by Category
### appetizer 1
![Very excellent interpretation of Universal construction by an example of Cartesian product](https://www.quora.com/Why-are-universals-significant-in-the-study-of-category-theory)

所以总体来看，universal construction 做了两件事情：
1. (pattern)**matching**
2. **ranking**(the recognized pattern)
3. **grouping** matched and unmatched

前两件是‘分内’,第三件事是‘副作用’，它可以对这个 pattern 肢解，并将其划分(grouping)成不同的分类.

而 **matching** 和 **ranking** 恰好也是一个搜索引擎要干的事情，所以 Bartosz Milewski 用搜索引擎来比喻一个 universal construction 简直太精髓了！


### appetizer 2
![excellent picture to illustrate the difference between imperative programming and functional programming](https://i.imgur.com/9LHCL8B.jpg)

> s ---(f1,f2)--- R1×R2

this diagram shows so explicitly what is a functional programming:
* imperative programming: 
    - we think about how to **combine the return of function**
    - (f(x1), f(x2))
* functional programming:
    - we think about how to **combine the function themself**
    - (f1,f2)(x)

why we think like that in FP, because the Category theory:
> What we have is just object and arrow, no elements, no elements, no elements.

### Dining
![Cartesian product in category](https://i.imgur.com/GMuwx63.jpg)

> tips: the 'fst' and 'snd' in picture above, is something like tuple._1 and tupe._2 in scala. And when you know something about the universal constrction, you know what is the ture power of pattern match in scala, and the hidden mathematical principle behind it.

In category theory, the 'fst' 'snd' function in haskell, and '._1' and '._2' is called **factorizing morphism**

[FAQ]
1. waht if m is bad: non-injective and non-surjective, it will lose information
    - p * m = p' : p' factorizes into q times m (if we see * as a product)
    - q * m = q' : q' factorized into q times m
    extract a common factor from p' and q'. so this m which as a morphism is very special
    take the worst out of projection q' and p', condenses them, then you can do nice thing, do the real projection.  why m is the worst thing.
    - Goldilocks principle: some candidates are just too big; others are just too small.
    - 'm' as a morphism can lose information, and shrunk.
    - p is clean for production, but when p combine with 'm',which m is dirty --- non-injective or non-surjective. then you will get p', is also bad thing.(means not clean enough)
2. non-surjective bad m example:
    - c = (Int, Bool)
    - a = Int; b = Bool; 
    - p = fst(a,_)=a ; q = snd(_,b) = b
    - c' = Int // bad
    - p'::Int->Int = id
    - q'::Int->Bool = ture
    - m::Int->(Int,Bool)x =(x,True)
    - morphism m from c' to c is non-surjective, because it miss pairs of the form(x,false)
    - missing infomation: ![missing information](https://i.imgur.com/IUmrer5.jp)
3. non-injective bad m example:    
    - c = (Int, Bool)
    - a = Int; b = Bool; 
    - p = fst(a,_)=a ; q = snd(_,b) = b
    - c' = (Int,Int,Bool)  // bad
    - p'::(Int,Int,Bool)->Int = p'(x,_,_) = x
    - q'::(Int,Int,Bool)->Bool = q'(_,_,b) = b
    - m::(Int,Int,Bool)->(Int,Bool)x = m(x,y,b)=(x,b)
    - morphism m from c' to c is non-injectve, because it miss pairs of the form(x,false)
    - redundent information: ![3d -> 2d](https://i.imgur.com/gQxQwHb.jpg)
4. so I must do ranking, say that pattern(c,a,b,p,q) is better than(c',a,b,p',q')  
    - because all the candidates have some flaw, that all the flaw is distilled with m.
    - m is not clean: see [[why m is the worst thing]]
8. Define product in Category(or what is product in Category theory)

    ![Category product](https://i.imgur.com/nRdqs8S.jpg)
    - 3 objectrs with 2 arrows(form 2 projection) 
    - universal properties: for any other object with two projections, so for any other c' that has some p' and q'
    - there is **uniqure** morphism m:: c' -> c
    - p' = p * m
    - q' = q * m

    **unique** here has some important means, which can get hints from:
    > any path (function composition) to terminal object will shrunk to a single unique arrow.
    > It turns out that terminal object is unique up to isomorphism.
    
    It's clearly that you should keep in mind what we are doing is **define the production in Category**, which only allows:
    1. use and ONLY use functions(arrow)
    2. production must has some pattern(universal propertiy)
    3. pattern will give many many production-like things
    4. there must exist the best one, and any other same pattern things will have one unique morphism to this best one.
    5. why? refer to the uniquness of the terminal object.
    6. this **unique** exclude the non-surjective and non-injective morphism.
    7. also makes a commutative diagram.
    

9. commutative diagram(33:15)
> In mathematics, and especially in category theory, a commutative diagram is a diagram such that all directed paths in the diagram with the same start and endpoints lead to the same result.
> Commutative diagrams play the role in category theory that equations play in algebra (see Barr–Wells, Section 1.7).

![commutative diagram in universal construction](https://s14.postimg.org/uq3js3zsx/screenshot_13.png)

picture above, shows 2 commutative diagram:
    1. c' -> c -> a + c' -> a
    2. c' -> c -> b + c' -> b


10. Not every Category has product, even has, not all pairs object have, but if Category has product, then it's a nice category, just like the category of sets, because every 2 sets in **category of sets**(which is model of our programming,remember that) have a product
11. if we want to imitate a Set category, need: initial/terminal object, product, coproduct(opposite of product)



