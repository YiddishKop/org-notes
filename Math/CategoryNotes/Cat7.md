# Cat 7.1 Functoriality, bifunctors
[lecture review]
- Functor is mappings between category;
- Endofunctor is mapping with in a category.
- Huge of functions putting together
- one major function map objects
- preserve the structure of category
- mapping between hom-sets
- if no connection will not maping; if has will not be destroyed
- preserve the composition and identity.
- **object to object** --- type constructor F, like List/Seq/Option
- **hom-set to hom-set**  --- fmap :: (a->b)->(Fa->Fb), F is type constructor.
- ordinaty functor = type constructor + fmap
- everything we defined for function is suit for functor, like injective and surjective
- List is function, function is list
- function is exponential datatype



## composition of functors

![composition of functors](https://s31.postimg.org/o78sbt1rf/screenshot_29.png)

now functors can **composable**, and also **identity**, and also **assoiative**.

titter :)

functors can be a category!

In **functor category**(or called category of functors) **functor** are **morphisms**.

what is functor? he is mapping of categories.
what is function? he is mapping of objects.

so, **category** is the **object** of **functor category**, so category in functor category has another name **cat**.

``` haskell
tail :: [a] -> [a] //not safe for empty list
```
> [a] is like List[A] in scala

we now learned the functor category, so we can define a `safeTail`

``` haskell
safeTail :: [a]->Maybe[a]
safeTail [] = Nothing
safeTail (x: xs) = Just xs
```
> note that:
> 1. [a] is functor; Maybe[a] is functor;
> 2. safeTail is a mapping of functors;
> 3. like functor is a mapping of categories, safeTail is a functor of functor categories

seriously, :|
remember `fmap`? 
`fmap` is a mapping of functions;
`safeTail` is a mapping of functors;

we may should try using fmap

**fmap will always go inside of container(functor), and apply the operation on the inside things, and again put it back into the container.**

seriously, :|
1. now I find that, haskell has a syntax type as lisp: all operator and function are prefix, damn it. 
2. because function is list, and list is function. so in scala, we can apply `fmap` twin `map` to `Collections`, although the signiture of fmap is a mapping from function to function.


``` haskell square on the Maybe
mis :: Maybe[Int]
sq :: Int -> Int
fmap( fmap sq ) mis
// same with
(fmap . fmap) sq mis
// remeber that, (a->b)->(Fa-Fb) => ((a->b)->Fa) -> Fb ,freeedom
```
> note that: 
> 1. `fmap sq` is applying fmap to a function, you get a function
> 2. `fmap( famp sq )` is applying fmap to the function return from **step(1)**, again get a function
> 3. funcion from **step(2)**, takes `mis` as parameter, operate on inside value of `mis` getting another value, then put it back into the container.

this is how you compose the functors in haskell


we mentioned previous lecture that, almost all the type constructor in haskell will automatically be a functor, because regular data structure in haskell are algebraic data types, all these algebraic data types are **automatically functorial**. And algebraic data types have some **operations** like product(-type), sum(-type), exponential(-type).

> so in algebraic datatypes' eyes, the `Either/Option/Try/Future` are same as `+` in algebraic, they are both operation
> so in algebraic datatypes' eyes, the `collections` are same as `*` in algebraic, they are both operation
> so in algebraic datatypes' eyes, the `functions` are same as `^` in algebraic, they are both operation

when you use these "operaion" on algebraic datatypes, you automatically get a functor, and a 1-to-1 relationship will build up:

## Product functor

`(a,b)` is a product-type, when can rewrite in another fomr `(,) a b`, and when we **fix a** ,is it a type constructor of b. Something like 

``` haskell
type X = (,) a
X b
```
`X` now is a type constructor of b, a functor on b, a contrainer of b. Now we can apply function to b, by fmap, we just illustrate it:

![type constructor only on 2nd type variable](https://s9.postimg.org/cm4dmxum7/screenshot_30.png)

of couse it could do ,and the related scala code is like: a reference to [type constructor used in scala's function](https://typelevel.org/blog/2016/08/21/hkts-moving-forward.html)

---
``` scala
// original, as above
def tuplef[F[_], A, B](fa: F[A], fb: F[B]): F[(A, B)]
```

``` scala
// F = List
def tupleList[A, B](fa: List[A], fb: List[B]): List[(A, B)]
```

``` scala
// F = Option
def tupleOpt[A, B](fa: Option[A], fb: Option[B]): Option[(A, B)]
```

More complicated and powerful cases are available with other kinds of type constructors, **such as by partially applying**. That’s how we can fit State, Either, and other **such types with two or more parameters into the F parameter**.

``` scala
// F = Either[E, ...]
def tupleEither[E, A, B](fa: Either[E, A], fb: Either[E, B]): Either[E, (A, B)]
```

``` scala
// F = State[S, ...]
def tupleState[S, A, B](fa: State[S, A], fb: State[S, B]): State[S, (A, B)]
```

Just as with double, though this isn’t the whole story of tuplef, its true meaning arises from the common way in which it treats all possible F arguments. That is where higher kinds start to get interesting.

---

### Define a functor of 2 categories by extending existing functor
Instead of definging a functor of 2 arguments --- these 2 arguments are types(objects) of ONE category, can we define a functor of TWO categories: one type(object) from one category, the other (type)obj from another category.

Further more, we can define a product of two categories, then functor from the product of categories would be a functor of two arguments, of course.

But product of categories will be something too complex, even product in ONE set category would use some universal construction.

NO~~~ product of 2 categories is really easy to define, easiser than the product in set category, at least for SMALL category --- which is objects in a category from sets.

  > small category
  > A category C is called small if both ob(C) and hom(C) are actually sets and not proper classes, and large otherwise. A locally small category is a category such that for all objects a and b, the hom-class hom(a, b) is a set, called a homset.
  > simply speeking, small category has two set: One set of objects, One set of arrows --- hom-set.

1. object of product category

    So we define a product category, and all objects inside are pair(or called Tuple), and is the product of the set of objects in two categories. It's easy, aren't they, because in small category, objects are in a set, so you have two category means you have two sets of objects, set can do Cartesian Product. ===> The product category has object as a pair in it.

2. arrow of product category

    But, how to do with morphisms(arrows). This is same thing you know, becasue the small category has all arrows in a hom-set, and hom-set is set, it can also do Cartesian Product. ===> The product category has arrow as a pair in it.

3. proving composition

    So we have new category( not prove identity, composition and identity yet), and we have objects(a pair) and arrows(a pair), Now if we can prove the composition identity associativity, then we truely have a new category, a product category

    ![Proving the composition](https://s9.postimg.org/jfiz88m2n/screenshot_32.png)
4. proving identity

    we also have identity: `(id, di) = id`

5. proving associative
    
    easy, skipped.


we now have a product category, then we can move forward to bifunctor

### Bifunctor

```
C × D ---> E
```

Bifunctor is just a functor for the product category, a mapping between a product category and a category. But as you know, we want a product category in Haskell, because the category is ONE category will object are type and arrow are functions, so product category is:

```
C × C ---> C
```

`C` is the Haskell, so what we are doing for product category is:

```
Haskell × Haskell ---> Haskell 
```

yes, we get it~:

``` haskell
a × b ---> (a,b)
```

### How to define a Bifunctor
In this scenario ,we Lift two functions at same time to combine them to a pair of function, which is an arrow in new product categoy, so we can say:
``` haskell
class Bifunctor f where
  bimap :: (a->a') -> (b->b') -> (f a b -> f a' b')
```
`f` is two type variable functor(or constructor), like something in scala: `Map[_,_]` or `Function[_,_]`.So, product is a bifunctor.

![Functor vs. BiFunctor](https://s9.postimg.org/f1f3a2vq7/screenshot_33.png)

Seriously :|
By now I find that, **Functor is what we say the type constructor with a map(which do operte unboxing and boxing) inside.**

Nothing else.



## Sum functor
Then you may think, we have **product functor** now, what about **sum functor**?

No worries, we can use the same principle of BiFunctor, apply to sum functor.

`Either a b` is a **sum-type**, but you should notice that we describe it by a **BiFunctor manner**.

`Either a b` takes a pair of types, OK pair of types is a product category, like we have find above. Instead of every object and arrow is **tuple pair** --- 

(
  * for object in product category: `(,) a b` 
  * for arrow in product category: `(,) f g`

),

they should **eigher pair** --- 

(
  * for object in "eigther" category: `eigher a b`
  * for arrow in "eigther" category: `eigher f g`

),

in this sum-type scenario.

the ONLY difference is `fmap`, you must use a case clause to match one type or the other one.


## summary for `C × C -> C`
here we have two kinds of functor: product-functor and sum-functor, they can be both decribed by `C×C->C` --- BiFunctor form.

Actually in any category, if you have products defined for all pair of objects, like two: product-functor and sum-functor above, we have another name for that category: **Cartesian Category**

> C × C -> C  ,  BiFunctor   , Cartesian Category.

And the same is true about the **coproduct**, **coproduct is also a BiFunctor**, long ago from now we defined coproduct just by the objects, but now we should define the coproduct also for morphism(arrow), just like what we do for product-functor above.

So, what we want to prove, I want to show that this is bifunctor I have to show that I can lift this pair `(f,g)` to something that there is a unique morphism between `a × b` and `a' × b'`. But how can I do this, if we compose f and p, compose q and g, we will find something familiar. 

yes, `a × b` become one candidate of `a' × b'` with two projections `a'` and `b'`. So, there must be a unique morphism between the `a × b` and `a' × b'`, we call this morphism `f × g` and this is "but now we should define the **coproduct also for morphism(arrow)**"  --- the coproduct lifting.

![prove coproduct is a bifunctor](https://s18.postimg.org/oq1s9cpih/screenshot_34.png)


## Monoidal Category 1
That is **categorical product**, not just only a **pair**, that's a cartesian category, it's a bifunctor, and if we have a coproduct in a category, we will have some co-Cartesian category. Then the coproduct is a bifunctor as well. So we have a category that has a bifunctor more general that just product or coproduct, maybe there are other bifunctors. So this kind of category have a bifunctor are called **monoidal category** ,
  * **bifunctor** is like a **binary operater**.
  * for **unit** we will prove that next lecture.

titter :) , monoid again, you know, unit and associative

## Some concept shoud say again:

* Product category is `C * D -> E`
* but Product category in Haskell is just `C * C -> C`, --- Haskell is ONE Category
* So this is the same(?) thing with two arguments type constructor 
* Cartesian Category is another name of Product category
* Monoidal category is that we have a bifunctor(simply speeking, two arguments type constructor) like Map[_,_] on this Cartesian category.
* bifunctor of Monidal category is that binary operator of Monoid



# Cat 7.2 Monoidal Categories,Functoriality of ADTs, Profunctors

## Monoidal category 2
we'll not introduce all things about monoidal category, it's too abstract.

In the monoidal category we would like to define things like what does it mean to multiply two objects.

product category is something like a way of multiplying objects, you have object a and object b, you multiply them and get the product.Now we have one part of a monoid --- binary operation --- bifuncotr.

* monoid is for set category
    - binary operation is for elements of object set, or elements of hom-set.
    - for production, **unit** is singleton set `()`, terminal object up to isomorphism.
* monoidal category is product category wih operater bifunctor.
    - you can prove **unit** from graphic below.
    - you also can find **bifunctor**.

![Unit of monoidal category](https://s17.postimg.org/qk3c9ki7z/screenshot_35.png)

it means like something `F[A,Unit] = F[A]` in scala.

[notation]: dotted line means unique morphism.
[notation]: morphism from everyt object to terminal object(Unit) is unique.

I can do the same thing for coproduct, **unit would be the initial object**

What's the good name for this product that could be a coproduct or could be a bifunctor, it's called **tensor product**, So monoidal category has a **tensor product**. tesor product has a unit.

![tensor product and unit](https://s17.postimg.org/z519e7mu7/screenshot_36.png)

### go back to haskell
Haskell is really a monoidal category, because we had product something in product and co-product.
I start all this discussion because I said that ADT are functorial. So far we see that the **product** is functorial and coproduct is functorial, product type and sum type are functorial. 

stop noting at 12:13


1. constant type diff from type constructor ,deos not depend on type, but they depend on values ok?
2. constant functor is mapping any type to a black hole.

![mapping to black hole](https://s18.postimg.org/ykp94ihd5/screenshot_37.png)

``` haskell
data Const c a = Const c

instance Functor(Const c)// const c is partially appplied to const c a, its a type constructor for a, a functor like 'f' before.
  -- fmap:: (a->b)-> Const c a -> Const c b
???  fmap f (Const c) = Const c

data Identity a = Identity a
  fmap f (identity a) = Identity (f a)
```

for a container, Const c is very special, it is alwasy empty.

now we have functor, and identity, we can do composing.

if a type is ADT, it's must be a functor

``` haskell
data Maybe a = Nothing | Just a
Either () (Identity a)
// () can be Cons () a
```

every ADT can transform to a functor using this metohd.

``` haskell
{-# LANGUAGE DeriveFunctor #-}
data Maybe = ......
     deriving Functor
```

there is only one fmap(a theory can prove that, not refer deep here)

`(->) a b = a -> b`
``` haskell
newtype Reader c a = Reader ( c-> a)
fmap = (*) // remember that?
Op c a = Op (a->c)
fmap::(a->b) -> Op c a -> Op c b
                 //a->c   //b->c

```

Is this a bifunctor above?
![bad function](https://s18.postimg.org/sxsw76zgp/screenshot_38.png)

* a -> b
* a -> c
* b -> c // we can not get this function ???

If we have 'b->a' that's good, so a->b is bad, can we reverse?

C^Op -> D
a -> b
a <-C- b

in haskell, it's a opposite haskell category to haskell
This kind of functor has a name called **Contravariant** functor.

class Contravariant f where
  contrmap:: (b->a) -> (fa -> fb)

Contra functor is not a container, more like a Contra-conatiner


when refer to a **bifunctor**:

(->) a b     C^op X C -> C // you take a pair morphism, but 1st is flip to another side

This is called **Profunctor**,

class Profunctor p where
  dimap :: (a' -> a) -> (b -> b') -> p a b -> p a' b'
               f          g         (a->b)   (a' -> b')
                                      h
  // by f,g,h ,how to get a'->b'
  g * h * f


![Profunctor](https://s18.postimg.org/ajid2zhyh/screenshot_39.png)


lmap ?
rmap ?
