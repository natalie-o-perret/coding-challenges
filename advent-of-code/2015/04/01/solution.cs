using System.Diagnostics;
using System.Security.Cryptography;
using System.Text;

static int FindAdventCoin(string secretKey)
{
    using var md5 = MD5.Create();
    var number = 1;
    while (true)
    {
        var text = secretKey + number;
        var hash = md5.ComputeHash(Encoding.UTF8.GetBytes(text));
        // Check if first 2.5 bytes are zero (5 hex digits)
        if (hash[0] == 0 && hash[1] == 0 && (hash[2] & 0xF0) == 0)
        {
            return number;
        }
        number++;
    }
}

// Test cases with assertions
Debug.Assert(FindAdventCoin("abcdef") == 609043);
Debug.Assert(FindAdventCoin("pqrstuv") == 1048970);

// Read input and calculate result
var inputPath = Path.Combine("..", "input.txt");
var secretKey = File.ReadAllText(inputPath).Trim();

var result = FindAdventCoin(secretKey);
Console.WriteLine($"C#: {result}");
