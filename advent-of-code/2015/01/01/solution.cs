static void CalculateAndPrintFloor(string source) =>
    Console.WriteLine(source.Aggregate(0, (floor, character) => character switch
    {
        '(' => floor + 1,
        ')' => floor - 1,
        _ => floor
    }));

// both result in floor 0
CalculateAndPrintFloor("(())");
CalculateAndPrintFloor("()()");

// both result in floor 3.
CalculateAndPrintFloor("(((");
CalculateAndPrintFloor("(()(()(");

// also results in floor 3.
CalculateAndPrintFloor("))((((("  );

// both result in floor -1 (the first basement level).
CalculateAndPrintFloor("())");
CalculateAndPrintFloor("))(");

// both result in floor -3.
CalculateAndPrintFloor(")))");
CalculateAndPrintFloor(")())())");

var scriptDir = Directory.GetCurrentDirectory();
var inputPath = Path.Combine(scriptDir, "..", "input.txt");
CalculateAndPrintFloor(File.ReadAllText(inputPath));
