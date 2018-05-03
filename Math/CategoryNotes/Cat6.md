# Cat 6.1 Functors

## Motivation: From pattern to category to Functor
Functors is really really important, all the previous lecture are the introduction to Fuctors.

Mathmatisian will tell you what's important is natural transformations that you need functors in order to define natural transformation.

**What is really universal construction about**, it's able to define what it means to be like a perfect embodiment of an idea, eg. how do we define a product? we have infinite possibilities to define a product, how do we pick one. If this product exists, it's actually unique or **unique up to a unique isomorphism**.

And we have **2 types of Universal construction** that one for product and for Coproduct: projection and injection.

what is Functor?
In mathematics, you have 2 categories, Functor is a mapping from one to another.
when we talked product and coproduct, I used a little loose language about saying, we now have leaned 4 pattern for GOOGLE to search:
    1. terminal object
    2. initial object
    3. product
    4. coproduct

All your life is doing pattern matching, so you will not protest when we refer to it first, but In Category you need first define what is your **pattern** when you want to do pattern matching in a Category, **pattern** has to have a **structure**. What's "to have a structure" mean? **Category** itself is actually a definition of a **structure** --- just combination of dots and arrows.

> * category is a structure
> * pattern is a structure
> * pattern is category

Being able to recognize one category(pattern) inside of another category is the definition of pattern recognition. and category tell us how to formalize patten recognition.

> pattern like product and coproduct are just exmaples of limits and colimits, which will come in the letter lectures after we introduce the natual transformation.

So category to category, by recognition, yes, this is what we want, **Functors**.

we can think one category as a pattern or model and map it into another category and we recognize a match for this model or embed this model inside another category.

## Functors

Definition of Functor have layers of clause, do it one by one

If you map one category to another category, you really do:
1. map objects
    - since objects form a set , so this map is also a mapping of sets, what is mapping of set --- function! functions can be non/surjective or non/injective, and **all we have known about functions can be translated into one part of the definition of the factor**

Mapping preserve structure, sets have no structure(ONLY a bunch of elements), no structure at all.

by the way, because no structure in sets, it's hard to implement set from the point of view of computer hardware, because computer hardware is actually has structure everywhere. Using structured things to represent no-structured thing is hard.

> * category embodies structure
> * set has no structure
> * category embodies lack of structure

**How to represent set by category? or same way asking how to implement set by category?**
Discrete category, is a category that has no morphism(arrow) other than the identity morphism. because once you have arrows you have structure, so we must have a category with no sturcture in-side to implement a set.

![discrete category](https://s14.postimg.org/p3lfj95ip/screenshot_15.png)

we have talked about category of sets, which object is represented by set.

Now, lets take ONLY one set and make it as a category, this can be done with discrete category.

**If we want to preserve structure, we must mapping arrows**

> * arrow have structure;
> * mapping preserve structure;
> * we want to preserve structure;
> * we must mapping arrows


![Illustration of Functor](https://s14.postimg.org/8den7koqp/screenshot_17.png)

titter :), also we have Hom-set, remember that? Hom-set is set of arrows, so mapping between arrows, is mapping between sets, what is mapping between sets --- functions

> * arrow have structure;
> * mapping preserve structure;
> * we want to preserve structure;
> * we must mapping arrows
> * hom-set is set of arrows
> * mapping arrows is mapping hom-sets is mapping sets
> * mapping between sets is functions

So, Functor is really a huge potentially number separate functins.

titter :) again, Now, go on talking about **presvering structure**, what else something related to a structure in category  --- **composition**!

> * composition have structure
> * want to preserve structure
> * mapping preverse structure
> * we must mapping composition

seriously, :| , now the one key important point comes, what is really "preverse strcuture" mean? what are functor, what are not functor?

there so many mappings between one category hom-set to another category hom-set, ONLY the mappings between C(a,b) and C(Fa,Fb) who can satisfy:

` F(g*f) = Fg * Ff `

is Functor, and mapping after composition is equall to composition after mapping is what we called "**preserve the structure**".

> preserve structure <=> mp after comp = comp after mp

which means that 'F' preserve the composition relation of the orignial how-sets.

seriously, :| again, one more thing --- identity which is also arrow, should be preserve,and the same thing with above:

if and only if those mappings between C(a,a) and C(Fa,Fa) satisfy:

` Fid_a = id_Fa `

is Functor.


> Summarize:
> Functor is this kind of **mapping** of objects and morphisms that **preserve** the composition and identity


#### 3 other things should keepped in mind.

![many morphism to one morphism](https://s14.postimg.org/bugpag8ch/screenshot_16.png)

keep in mind that,

1. many morphism in orginal map to one morphism in target category is OK. because Functor is mappings, also means that he is functions, functions may shrink things, may collapse things, many:1 is function, right! it's OK. And any other attricute we talked about functions, is also suited for Functors. Functors doesn't have to be surjective or injective. But you CAN NOT destroy the connection(arrow) of original category.

2. Functors can collapse the objects, like 30 objects in original but 3 objects in target category.

3. EndoFunctor : original Category and target category are **same** one(no reqiurement that they should be different categories)

#### Two important definition of functor on hom-set

>> **Faithfull Functor** is injective on **hom-set** <<
>> **Full Functor** is surjective on **hom-set** <<
>> this two defnition ONLY related to home-set, not objects.

#### Two kinds of important Functors
1. Picking Functors: A functor just "picking" object from target category:

![every Functor is just picking one Object from target category](https://s14.postimg.org/rjruak2lt/screenshot_18.png)

arrows in this picture above, is two Functors, keep attention.

this is something like functions of singleton set


2. Constant Funtors(Δc): All collapse to black hole

arrows in this picture above, are Functors, keep attention.
![Constant functor](https://s14.postimg.org/wwgoog5v5/screenshot_19.png)


3. EndoFunctor : original Category and target category are **same** one(no reqiurement that they should be different categories)
In scala and Haskell, Functors are EndoFunctors, because they are all summed to ONLY have one category.

## application of functor in programming


### application 1 : type constructor.

``` hasekll
Mabe a
```

```
 new cate:      Maybe a            Maybe b
                   ^                   ^ 
                   .                   . 
                   .Maybe              .Maybe
                   .                   . 
                   .                   . 
 original cate:    a                   b
```

Functor is a mapping between whole types, yes, **type constructor**.

``` scala
List[A]
```
**`List`** is a Functor, he is a type constructor, which mapping from category **A** to category **List[A]**

``` scala
Option[A]
```
**`Option`** is a Functor, he is a type constructor, which mapping from category **A** to category **Option[A]**

This is only one use of functor, just mapping the objects(type). Functor can also mapping morphism

### application 2 : mappings between function

Indeed, functor can be a mapping between (mapping of type) and (mapping of type constructor)

``` hasekll
fmap::(a->b) -> (Maybe a -> Maybe b)
```

```
 new cate:       Maybe a ---------->Maybe b
                    ^        ^          ^ 
                    .        .          . 
                    .Maybe   .fmap      .Maybe
                    .        .          . 
                    .        .          . 
 original cate:     a --------------->  b
```
              
![Illustation of Functor](https://s14.postimg.org/puir2scpd/screenshot_20.png)

in an abstract way of commutative graph:

![commutative graph of Functor](https://s14.postimg.org/otn3qvq35/screenshot_21.png)

![Functor in haskell](https://s14.postimg.org/4pbx4spwx/screenshot_22.png)

when programming haskell ,we are straying from mathematics. Let's **define** a Functor: the definition below is an abstract Functor, or we define the template.
 
``` haskell
data Maybe a = Nothing | Just a
fmap :: (a->b) -> (Maybe a -> Maybe b)
fmap f Nothing = Nothing
fmap f (Just x) = Just (f x)
```

This is a typical way of implementing functors, **the functor usually has somthing of type `a` inside**, then you can apply this function to the inside of of a functor, in a moment I'll talk about this next lecture.

Instresting, professor ask a question: `fmap f Nothing = ?` can be somthing else other than Nothing?
then he says something about the polymorphism:

> Can it be something "it's Nothing unless A is integer."

> ad-hot polymorphism: for Integer do one thing, for non-Integer do other things.

> because kinds of polymorphism supported by Haskell is limited, so there is more restriction here we can do.

# Cat 6.2 Functors in programming

the last episode of previous lecture, we talked about the two important use of Functors:mapping obj and mapping functions

now we must make sure that the Functor should preserve the structure: composition and identity

It's a pity that Haskell compiler CANNOT check this two things, you must take a paper and draw some thing to guarantee that.

## Checking Functor preserving structure

> TARGET:
> [ ] 1. fmap id = id
> [ ] 2. fmap (g*f) = fmap g * fmap f

### "=" means replace with each other
notice that 1st id is the orignial 2nd is for target category, and symbol **=** means **equal** as it is in math, What is **"function equal"** means, yes it's means that **they can replace with each other on two sids of "="**, when you find somewhere one is called, you can replace directly by the other one, means they are actually the same thing.

![Perserving the comoposition](https://s14.postimg.org/avddb5u0h/screenshot_23.png)


### inline vs. refactory

* professor says that macro in C++ is an example of **inline**;
* replace equal method between each other **refactory**
* inline and refactory in imperative language is difficult; but in functional language is not so annoy

### Check Functor preserving identity

> TARGET: identity
> [ ] 1. fmap id = id
>    - [ ] 1. fmap id Nothing = Nothing
>    - [ ] 2. fmap id (Just x) = Just x
> [-] 2. fmap (g*f) = fmap g * fmap f

> PROVE TARGET
``` haskell
// fmap is the general name of Functor in Haskell
// f here is the function of original category
// we now need to justify the identity: fmap id = id
// if we want to do this, we need to ensure

data Maybe a = Nothing | Just a
fmap :: (a->b) -> (Maybe a -> Maybe b)
fmap f Nothing = Nothing
fmap f (Just x) = Just (f x)

id x = x

// also x = id x
// id Nothing = Nothing
// fmap f Nothing = Nothing

fmap id Nothing = Nothing

// fmap id Nothing = Nothing = id Nothing
// fmap id (Just x) = Just(id x) = Just x
```

So you can see that from code block above

> TARGET: identity
> [x] 1. fmap id = id
>    - [x] 1.1 fmap id Nothing = Nothing
>    - [x] 1.2 fmap id (Just x) = Just x
> [ ] 2. fmap (g*f) = fmap g * fmap f

> tips: keep in mind that, "=" in quotion block above , is as it is in mathematic, means equal

### Check Functor preserving composition
same with above, skipped here. then professor refer to **polymorphism** again, that "you can get ensurement for free of the **composition** by **polymorphism** in hasekll"

here are some reference to blogs about **profunctor**:
1. [contravariant Functors - An Intuition](http://igstan.ro/posts/2013-10-31-contravariant-functors-an-intuition.html)
2. [profunctor and polymorphism](http://igstan.ro/posts/2013-10-31-contravariant-functors-an-intuition.html)


### Something about the Functor in Haskell
when you define a Functor in Haskell, you think you truely get a functor, but you will find not that. Because in the next lecture you will most of the stuff you come up with is automatically a functor, like algebraic datatypes, it's automatically a functor.

Functor have his laws(preserve structure:mapping objects/functions, keep the composition and identity). While monad also has its own laws.

## A general Functor in Hasekll: lifting
why called lifting ,a picture to illustrate this, it's just some like higher-level of obstraction.

![Lifting](https://s31.postimg.org/6jcqp1orf/screenshot_24.png)

`fmap` shown above in code block is a **higher order polymorphic function**: it takes a function and produce another function:

``` haskell
fmap :: (a->b) -> (Maybe a -> Maybe b)
```

You'll see a different kind of polymorphism in which depending on what your parameters is, in this case the functor, you will get a different implementation of a function --- fmap in this case.


``` haskell
clss Eq a where
  (==) :: a -> a -> Bool
```
This is an ad-hoc polymorphism, which is parameterized here by "a" type, but with functors we have a slightly bigger problem, because functors are not parameterized by types, functors are actually type constructors.

If we want to define a functor we have to define it as a class, give the name( we don't need to specify it's a type or a type constructors) because the next line we'll show the proper code, and compiler will know that.

``` haskell
class Functor f where
  fmap :: (a->b) -> (fa->fb) // by this line, compiler will know f is a functor(type constructor)
```

In `fa->fb`, a is a type, then f can take type as parameter, so f is a functor(type constructor). And `fmap:: (a->b)` will imply that this **fmap** is a **polymorphic function** because it works for any way a and b. By the way this is slightly like the Function1 class in scala,and when we extends from Function1:

![functor in scala](https://s31.postimg.org/qctfvyp3f/screenshot_25.png)

## TODO

**In programming, what is a functor: it's just a type constructor that support fmap.**

### Functor example1 : List + fmap
In this sense, many `collection` with `map` function build in as API is a **Functor**:

``` scala
val c = List(1,2,3,4)
c.Map(a => a + 10) // List(11,12,13,14)
```

let's go back to the code about a list, of previous lecture:

`data List a = Nil | cons a (List a)`
It is so **self-explanatory** , and give a **recursive** definition of `List` 
> - "what is a List"
> - "it's empty or concate a value with a List"

``` haskell
class Functor f where // abstract class
  fmap :: (a->b) -> (fa->fb) // here f is a type constructor

data List a = Nil | cons a (List a) // List is a type constructor

instance Functor List where
  fmap g Nil = Nil
  fmap g (cons head tail) = cons (g head) (fmap g tail) // funny
```
last 3 line of code is just the **pattern match** function, something like scala **case match clause**. So, you can see somthing like `cons head tail`. And, `head` and `tail` are two variables used in pattern match clause, will be directly assign proper value when matched.

``` scala
def fn(lst: List[Int]) = lst match{
  case Nil => println("empty")
  case head :: tail => println("head: " + head + ", tail: " + tail)
}
```

Note that , `fmap g tail` is a recursive funtion using again `fmap g`

this code above is the map API of List, and map of List is just one implementation of fmap.

### Functor example2 : Reader + fmap

``` haskell
type Reader r a = r->a
```

type construnctor can be an **"Symbol"** itself:
> 1. List[Int]: List construct List[Int] from Int
> 2. Option[Int]: Option construct Option[Int] from Int
> 3. Seq[Int]: Seq construct Seq[Int] from Int

`List`,`Option`,`Seq`, are all **Characters**; but type constructor also can be "Symbol", like `->`,`=>`,`::`,`+:`, and even more we use **char-type-constructor** as **prefix**, here we can use **symbol-type-constructor** as **infix**:

> 1. =>[Int,Int]: => constuct Function[Int,Int] from Int,Int
> 2. ::[Int,List[Int]]: :: construct List[Int] from Int,List[Int]
> 3. +:[Int,Seq[Int]]: +: construct Seq[Int] from Int,Seq[Int]

 
another problem, **we never talk about two parameter type constuctor**, yes,but we can just fix one type and say we only care about the second, like we can do that in partial applied function.

> 1. Int => : is a type constructor on Int
> 2. Int :: : is a type constructor on List[Int]
> 3. Int +: : is a type constructor on Seq[Int]

```
(a->b) -> (Fa->Fb)
is same with
((a->b) -> Fa) -> Fb
F <=> r->
(a->b) -> (r->a) -> (r->b)
```

In scala, Function1[+A,-B] is just a two parameter type constructor, it will reduce to one type constructor when fix first parameter:

| haskell  | scala               |
|----------|---------------------|
| a -> b   | Function1[+A,-B]    |
| a -> = F | Function1[_,-B] = F |
| F b      | F[-B]               |


then `Reader r` is our Functor.

This is like curry or partial applied function, you have 2 arguments(must be 2 parameter list in scala),you fix one argument and it becomes a function of one argument here.


![fix one of two becomes a functor of the other one](https://s31.postimg.org/dtc3dfxbv/screenshot_26.png)

``` haskell
class Functor f where // abstract class
  fmap :: (a->b) -> (fa->fb) // here f is a type constructor

type Reader r a = r -> a // 'r ->' is a type constructor

fmap :: (a -> b) -> (r-> a) -> (r-> b)
// h is (a->b); g is (r->a)
fmap h g = h * g = (*) h g // this you get a function: r -> b
// fmap = * 
```

fmap h g = h * g = (*) h g
then fmap = * 

**this is function, you only have parameter h and g, so in your function body(all things after '=') should use and ONLY use this two parameters.**

you can compare these two Functor

``` haskell
class Functor f where // abstract class
  fmap :: (a->b) -> (fa->fb) // here f is a type constructor

data List a = Nil | cons a (List a) // List is a type constructor

instance Functor List where
  fmap h Nil = Nil
  fmap h (cons head tail) = cons (h head) (fmap h tail) // funny
```

![compare these two functors](https://s31.postimg.org/m4lc11v7v/screenshot_27.png)

serious :| , you must keep in mind that when you are ambiguous with code above, that is all the chars occur in the codes are type variable, **don't think them as value**, then you can understantd:
1. why `r->b` = `h * g`
2. why `h (cons head tail)` is pattern match.

### Pattern match in Haskell and Scala
```
fmap h Nil = Nil
fmap h (cons head tail) = cons (h head) (fmap h tail) // funny
```
pattern match in Haskell is something like code above, which in scala we must use case match clause, so you know that why in scala **case clause is also a function in scala**, it's truly imitate the stype and principle of the Haskell.

> pattern match in haskell used like function
> pattern match in scala --- case clause also can be used like function

## Intuition functor is container
The intuition is that a **functor** when it's acting on some type, it actually encapsuated the values of this type,it somehow hide them, the **functor** has this type's instance inside. Something has other things inside is usually called a **container**, so I like to think of **functors** as **containers**, eg `List`, `Seq`, `Array`, `Option` etc.

And what does it mean to apply a function to a functor or container, it means just open this container, look at the stuff that's inside the container and apply the function to content of the container(functor)

The most important about Functor is **you can apply a function to what it contains**, but Functor **dese not provide you a way of retrieving(search and get, so in scala it's not recommanded to use get() method of Future) this value**, that's not part of the definition of a Functor, so you don't know whether this value is there or is not there, all you know is that you can operat on it. Functor is some like a radioactive thing, you can take a gloves to operate on it, but you never take it out, you'll die.

> Functor:
> - can operate on
> - no retrieving

### Function is Data, Data is Function

**What is actually a List, What List is on the ground?**
you know that, 
* Boolean can be memoized. 
* List/String can not be memoized.

List can have inifinite elements, we may ask how was List represeted inside the computer? OK, it is **represented by function**. It just produce elements, but function can also produce element. Refer to List, what you know is just a symbol "List", and you give some values as initialization, like `List(1,2,3)`, then you ask value by given loacation like `l(2)`, so:
* `List(1,2,3)` is just giving the domain of function
* `l(2)` is just calling function by giving an input

so, **List is Function,and Function is a general List**

good reference: 

![useful graphic to illustrate](https://s31.postimg.org/u2kszvzez/screenshot_31.png)
[type constructor using in function](https://www.atlassian.com/blog/archives/scala-types-of-a-higher-kind)

From the link to graphic, we can see that:
> * List[_]  is (*->*)
> * Map[_,_] or Function1[_,_] is (*->*->*)
> * Map[Int,_] or Function1[Int,_] is (*->*)
> * Functor[F[_]] is ((*->*)->*)

`*->*` This says: given one type, produce another. For instance, given String produce the type List[String].
All the type constructor list above, can apply partially: **Map[Int,_] or Function1[Int,_] is (*->*)**


Everything in haskell, is just thunk, there is no hard core distinction, then what function type is in category theory actually, you'll see that function type is just an exponential data type.

so, **Functin is just a exponential data type**

> Many data:
> "may or" is sum type;
> collection is product type;
> function is exponential type;


```
(a->b) -> (Fa->Fb)
```
(1) F = List : is a container(functor) implemented by product-datatype
(2) F = r -> : is a container(functor) implemented by exponential-datetype
