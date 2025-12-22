void FindAndPrintBasementPosition(string source)
{
    var floor = 0;
    for (int position = 0; position < source.Length; position++)
    {
        var character = source[position];
        
        if (character == '(')
            floor++;
        else if (character == ')')
            floor--;
        
        if (floor == -1)
        {
            Console.WriteLine(position + 1); // 1-indexed
            break;
        }
    }
}

// causes him to enter the basement at character position 1
FindAndPrintBasementPosition(")");

// causes him to enter the basement at character position 5
FindAndPrintBasementPosition("()())");

var instructions = File.ReadAllText("../input.txt");
FindAndPrintBasementPosition(instructions);
