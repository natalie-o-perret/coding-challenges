using System;
using System.IO;
using System.Linq;

bool IsNice(string s)
{
    // Check for a pair that appears at least twice without overlapping
    bool hasPair = false;
    for (int i = 0; i < s.Length - 1; i++)
    {
        string pair = s.Substring(i, 2);
        // Look for the same pair starting at least 2 positions later
        if (s.IndexOf(pair, i + 2) >= 0)
        {
            hasPair = true;
            break;
        }
    }
    if (!hasPair)
    {
        return false;
    }

    // Check for a letter that repeats with exactly one letter between
    bool hasRepeat = false;
    for (int i = 0; i < s.Length - 2; i++)
    {
        if (s[i] == s[i + 2])
        {
            hasRepeat = true;
            break;
        }
    }

    return hasRepeat;
}

// Test cases with assertions
System.Diagnostics.Debug.Assert(IsNice("qjhvhtzxzqqjkmpb") == true);
System.Diagnostics.Debug.Assert(IsNice("xxyxx") == true);
System.Diagnostics.Debug.Assert(IsNice("uurcxstgmygtbstg") == false);
System.Diagnostics.Debug.Assert(IsNice("ieodomkazucvgmuy") == false);

// Read input and calculate result
string inputPath = Path.Combine("..", "input.txt");
string[] strings = File.ReadAllLines(inputPath);

int result = strings.Count(IsNice);
Console.WriteLine($"C#: {result}");
