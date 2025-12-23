using System.Security.Cryptography;
using System.Text;

static int FindAdventCoin(string secretKey)
{
    using var md5 = MD5.Create();
    var number = 1;
    while (true)
    {
        string text = secretKey + number;
        byte[] hash = md5.ComputeHash(Encoding.UTF8.GetBytes(text));
        // Check if first 3 bytes are zero (6 hex digits)
        if (hash[0] == 0 && hash[1] == 0 && hash[2] == 0)
        {
            return number;
        }
        number++;
    }
}

// Test cases - skipped for Part 2 (would take too long)

// Read input and calculate result
var inputPath = Path.Combine("..", "input.txt");
var secretKey = File.ReadAllText(inputPath).Trim();

var result = FindAdventCoin(secretKey);
Console.WriteLine($"C#: {result}");
