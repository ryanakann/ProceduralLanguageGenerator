# ProceduralLanguageGenerator

## Overview

The goal of this project is serve as a utility tool for writers to quickly generate a complete unique language in a matter of seconds based on a small subset of input parameters. Languages are beautiful and plentiful, and a lot of books I read are severely underutilizing the range of potential that a language can provide.

## Deliverable

A downloadable language language model whereby you can plug it into a program, and have that program convert any input in english to the translation in the procedurally generated language.

## Example of a Cringe Language

Here's Krakish from the Guardians of Ga'Hoole series:
https://guardiansofgahoole.fandom.com/wiki/Krakish

As you read through, you'll pretty quickly see that this language is just a blend of Germanic and Norse languages with some funny sounds. Massive L.

## Example of a Based Language

https://en.wikipedia.org/wiki/Elvish_languages_of_Middle-earth

My man's got an etymological dictionary. Who does that?

## Background

I am not a linguist, but I do like learning languages and am at the very least aware of some of the basic flavors of English, Spanish, Italian, Chinese, and Japanese. 

I also am an avid fan of nerdy linguistics YouTube and Conlang shenanigans. Here are some of my favorite videos if you're interested:

1. [I removed most of the syllables from english and it's 30% faster now][glish]
1. [Seraphim: An Angelic Conlang for Agma Schwa's Cursed Conlang Contest][seraphim]
1. [Uppestcase and Lowestcase Letters [advances in derp learning]][uppestcase]

## Plan

To be honest I don't really know what I'm doing. My current plan is to take a bunch of random things I know about languages and try to mix those together into something coherent.

### Phase 1

Create a procedurally generated encoding of English based on the Sonority Sequencing principal as described in the [Glish video][glish]. This will be a simple encoder that takes in English sentences as input and outputs some mapping of words in Kenyon and Knott (KK) spelling.

### Phase 2

Assign sounds or sequences of sounds in the KK output above to alphabetical characters. Here are some examples using real languages:

* /ʧ/ -> English -> ch -> Example: chime
* /ʧ/ -> Italian -> c or cc -> Example: Vinci
* /ʧ/ -> Chinese (Pinyin) -> q or ch depending on the word ending. -> Example: qi or chi

### Phase 3

Randomize the syntax. Not everything follows the same ordering as English. Here's an example of the potential differences. (Note that these are not hard-set rules. Some of these have flexibility without sacrificing the meaning of the sentence, though it may or may not sound unnatural.)

* English: (Determiner) + (Adjective) + Subject + (Adverb) + Verb + (Determiner) + (Adjective) + Object + (Prepositional Phrase) + (Conjunction) + (Independent Clause)
* Chinese: (Time) + (Subject) + (Place) + (Manner) + Verb + Object + (Subordinating Conjunction) + (Subordinate Clause)

This will require a lot more research into various sentence structures as well as a mechanism for parsing them.

### Phase 4

Procedurally generated associated written language. To be honest this could be a complete project on it's own. This sounds really hard, but I think I have an interesting lead on potential techniques from Suckerpinch's [Uppestcase and Lowestcase video][uppestcase]


[glish]: https://www.youtube.com/watch?v=sRbcw2sGkJw
[seraphim]: https://www.youtube.com/watch?v=EOctKnETWi4
[uppestcase]: https://www.youtube.com/watch?v=HLRdruqQfRk
