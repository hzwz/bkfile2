<?php
/*
 * @Author: your name
 * @Date: 2019-11-15 13:46:12
 * @LastEditTime : 2019-12-24 15:15:02
 * @LastEditors  : Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: 
 */
error_reporting(0);
$path=$_POST["path"];
$file=$_POST["file"];
header("Content-type: text/html; charset=utf-8");

function getDir($path){
 
    if(is_dir($path)){
   
      $dir = scandir($path);
      foreach ($dir as $value){
        $sub_path =$path .'/'.$value;
        if($value == '.' || $value == '..'){
          continue;
        }else if(is_dir($sub_path)){
          echo 'is_directory:'.$path.'/'.$value .'::::::';

        }else{
          //.$path 可以省略，直接输出文件名
          echo ' is_file:'.$path. '/'.$value.'::::::';
        }
      }
    }
  }

if($path){
    getDir($path); 
}
if($file){
    echo readfile($file);
}
