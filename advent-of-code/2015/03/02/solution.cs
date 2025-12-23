using System.Diagnostics;

static int CountHousesWithRobo(string directions)
{
    var santaX = 0;
    var santaY = 0;
    var roboX = 0;
    var roboY = 0;
    var visited = new HashSet<string> { "0,0" };
    
    for (var i = 0; i < directions.Length; i++)
    {
        char c = directions[i];
        if (i % 2 == 0) // Santa's turn
        {
            switch (c)
            {
                case '^': santaY++; break;
                case 'v': santaY--; break;
                case '>': santaX++; break;
                case '<': santaX--; break;
            }
            visited.Add($"{santaX},{santaY}");
        }
        else // Robo-Santa's turn
        {
            switch (c)
            {
                case '^': roboY++; break;
                case 'v': roboY--; break;
                case '>': roboX++; break;
                case '<': roboX--; break;
            }
            visited.Add($"{roboX},{roboY}");
        }
    }
    
    return visited.Count;
}

// Test cases with assertions
Debug.Assert(CountHousesWithRobo("^v") == 3);
Debug.Assert(CountHousesWithRobo("^>v<") == 3);
Debug.Assert(CountHousesWithRobo("^v^v^v^v^v") == 11);

// Read input and calculate result
var inputPath = Path.Combine("..", "input.txt");
var directions = File.ReadAllText(inputPath).Trim();

var result = CountHousesWithRobo(directions);
Console.WriteLine($"C#: {result}");
