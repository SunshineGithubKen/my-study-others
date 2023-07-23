<?php

class Post
{
  private $text;

  public function __construct($text)
  {
    if (strlen($text) <= 3) {
      // echo 'Text too short!' . PHP_EOL;
      // exit;
      throw new Exception('Text too short!');
    }
    $this->text = $text;
  }

  public function show()
  {
    printf("%s" . PHP_EOL, $this->text);
  }
}