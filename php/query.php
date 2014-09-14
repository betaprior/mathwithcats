<?php
$questions = [
  ['title'  => 'The title of an algebra question', 
   'body'   => 'The body of the algebra question.',
   'options' => ['Option 1',
                 'Option 2',
                 'Option 3',
                 'Option 4',
                 'None of the Above'],
    'answer' => '2', 
    'tags'  => ['algebra',
                'prime-numbers', 
                'divisibility']],
  ['title'  => 'The title of a probability question', 
   'body'   => 'The body of the probability question.',
   'options' => ['Option 1',
                  'Option 2',
                  'Option 3',
                  'Option 4',
                  'None of the Above'],
    'answer' => '3', 
    'tags'  => ['probability', 
                'statistics', 
                'brownian-motion']],
  ['title'  => 'The title of a Calculus question', 
   'body'   => 'The body of the calculus question.',
   'options' => ['Option 1',
                  'Option 2',
                  'Option 3',
                  'Option 4',
                  'None of the Above'],
    'answer' => '1', 
    'tags'  => ['calculus', 'algebra', 
                'analysis', 
                'differential-calculus']]];

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