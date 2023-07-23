関数の仕組みを理解しよう：
関数の作成と呼び出し方法
引数と返り値（戻り値）の扱い
組み込み関数とユーザー定義関数

返り値のない関数を作ろう：
返り値のある関数と返り値のない関数の違い
return文の使い方とNoneの省略

引数のデフォルト値を指定しよう：
引数にデフォルト値を設定する方法
デフォルト値指定時の注意点

変数のスコープを理解しよう：
ローカル変数とグローバル変数の概念
変数のスコープとスコープの範囲

＃Dotinstallより

Creating and Calling Functions:
Functions are blocks of code with a name that perform a specific task and can be reused to avoid code duplication.
To create a function, use the def keyword followed by the function name and any required arguments.
The code inside a function is indented and executed when the function is called.
To call a function, use its name and provide any necessary arguments.

Handling Arguments and Return Values:
Functions can accept arguments, which are variables that hold values passed to the function.
Arguments allow functions to work with different data or perform operations based on input.
Functions can also return values using the return statement, which allows them to send results back to the caller.

Built-in Functions and User-Defined Functions:
Python provides built-in functions that are readily available for common operations (e.g., print(), len()).
User-defined functions are created by the programmer to encapsulate specific tasks.

Creating Functions without Return Values:
Functions that do not return any value are called "void" or "non-returning" functions.
They perform a task but do not provide any output or result.
To indicate the absence of a return value, Python uses the special None value.

Specifying Default Values for Arguments:
You can set default values for function arguments, allowing callers to omit those arguments if desired.
Default values are specified in the function definition using the assignment operator (=).

Considerations for Default Value Specification:
When using default values for arguments, ensure that arguments with default values come after those without defaults.
This ensures that arguments are assigned correctly when calling the function.

Understanding Variable Scope:
Variables in Python have different scopes, which determine where they can be accessed.
Local variables are defined within a function and are only accessible within that function.
Global variables are defined outside any function and can be accessed from anywhere in the program.

Scope and Scope Range of Variables:
The scope of a variable refers to the part of the program where the variable is accessible.
Local variables have a limited scope within the function where they are defined.
Global variables have a broader scope and can be accessed from any part of the program.