<?php
$questions = [
  ['title'  => '---', 
   'body'   => '
    Three cards are pulled from a deck of $52$ cards.  The probability of obtaining at least one club is:
   ',
   'options' => ['$\dfrac{_{39}P_{3}}{_{52}P_{3}}$',
                 '$1-\dfrac{_{39}P_{3}}{_{52}P_{3}}$',
                 '$\dfrac{_{39}C_3}{_{52}C_3}$',
                 '$1-\dfrac{_{39}C_3}{_{52}C_3}$'],
    'answer' => '2', 
    'tags'  => ['probability']],
    
  ['title'  => '---', 
   'body'   => '
    If a fair six-sided die is tossed twice, the probability that the first toss will be a number less than $4$ and the second toss will be a number greater than $4$ is:
   ',
   'options' => ['$1/3$',
                 '$5/6$',
                 '$1/6$',
                 '$3/4$'],
    'answer' => '2', 
    'tags'  => ['probability']],
    
  ['title'  => '---', 
   'body'   => '
    Two fair six-sided die are rolled and the face values are added.  The probability of obtaining an odd number greater than $8$ is:
   ',
   'options' => ['$1/6$',
                 '$2/9$',
                 '$1/9$',
                 '$1/4$'],
    'answer' => '2', 
    'tags'  => ['probability']],  

  ['title'  => '---', 
   'body'   => '
    A jar contains $3$ chocolate chip cookies and $x$ oatmeal cookies.  Two cookies are pulled from the jar without replacement.  An expression that represents the probability one cookie is chocolate chip and the next cookie is oatmeal is:
   ',
   'options' => ['$\left(\dfrac{3}{x+3}\right)\left(\dfrac{x-1}{x+2}\right)$',
                 '$\left(\dfrac{3}{x+3}\right)\left(\dfrac{x}{x+2}\right)$',
                 '$\left(\dfrac{3}{x+3}\right)\left(\dfrac{x-1}{x+2}\right)$',
                 '$\left(\dfrac{3}{x+3}\right)\left(\dfrac{2}{x+2}\right)$'],
    'answer' => '2', 
    'tags'  => ['probability']],
    
  ['title'  => '---', 
   'body'   => '
    In a playoff series, the probability that Team A wins over Team B is $3/5$ and the probability that Team C wins over Team D is $4/7$.  If the probabilities are independent, the probability that Team A wins and Team C loses is:
   ',
   'options' => ['$9/35$',
                 '$12/35$',
                 '$7/12$',
                 '$1/3$'],
    'answer' => '2', 
    'tags'  => ['probability']],
    
  ['title'  => '---', 
     'body'   => '
      A $5$ digit PIN can begin with any digit (except $0$) and the remaining digits have no restriction.  If repeated digits are allowed, the probability of the PIN beginning with a $7$ and ending with an $8$ is:
     ',
     'options' => ['$1/10$',
                   '$2/5$',
                   '$1/100$',
                   '$1/90$'],
      'answer' => '2', 
      'tags'  => ['probability']],
      
  ['title'  => '---', 
   'body'   => '
    Two cards are drawn without replacement from a deck of $52$ cards.  The probability of the first card being a red face card and the second card being a club is:
   ',
   'options' => ['$1/34$',
                 '$3/104$',
                 '$19/52$',
                 '$9/22$'],
    'answer' => '2', 
    'tags'  => ['probability']],
    
  ['title'  => '---', 
   'body'   => '
    In a bag, there are 11 red marbles, 8 blue marbles, and 3 white marbles in the bag.  What&#8217;s the probability of selecting of randomly selecting a blue marble from the bag?:
   ',
   'options' => ['$.275$',
                 '$.364$',
                 '$.375$',
                 '$.500$'],
    'answer' => '2', 
    'tags'  => ['probability']],
    
  ['title'  => '---', 
   'body'   => '
     The probability that a white adult man with a high white blood count contracts leukemia is $0.35$.  A proper interpretation of this probability is:
   ',
   'options' => ['There&#8217;s a $35%$ chance that a randomly selected white adult man will contract leukemia.',
                 'Three out of every five white adult men with a high white blood count will contract leukemia.',
                 'There&#8217;s a 65% chance that a randomly selected white adult man with a high white blood cell count will contract leukemia.',
                 'We&#8217;d expect that, in a sample of 100 white adult men with high white blood cell counts, 35 will contract leukemia.'],
    'answer' => '2', 
    'tags'  => ['probability']]
  ];

function filter($questions, $keyword){
  $filtered = [];
  foreach($questions as $question){
    if( matchesKeyword($question, $keyword) )
      array_push($filtered, $question);
  }
  return $filtered;
}    

function matchesKeyword($question, $keyword){
  $tagList = $question['tags'];
  $matchFound = false;
  foreach($tagList as $tag){
    if($tag == $keyword)
      $matchFound = true;
  }
  return $matchFound;
}

/*echo "<pre>";    
  print_r( filter($questions, $_GET['key']) );
echo "</pre>";*/
echo json_encode( filter($questions, $_GET['key']) );
?>