using System.Diagnostics;

static int CountHouses(string directions)
{
    var x = 0;
    var y = 0;
    var visited = new HashSet<string> { "0,0" };
    
    foreach (var c in directions)
    {
        switch (c)
        {
            case '^': y++; break;
            case 'v': y--; break;
            case '>': x++; break;
            case '<': x--; break;
        }
        visited.Add($"{x},{y}");
    }
    
    return visited.Count;
}

// Test cases with assertions
Debug.Assert(CountHouses(">") == 2);
Debug.Assert(CountHouses("^>v<") == 4);
Debug.Assert(CountHouses("^v^v^v^v^v") == 2);

// Read input and calculate result
var inputPath = Path.Combine("..", "input.txt");
var directions = File.ReadAllText(inputPath).Trim();

var result = CountHouses(directions);
Console.WriteLine($"C#: {result}");
