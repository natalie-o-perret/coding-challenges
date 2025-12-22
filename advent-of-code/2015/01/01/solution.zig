const std = @import("std");

fn calculateAndPrintFloor(source: []const u8) void {
    var floor: i32 = 0;
    for (source) |character| {
        switch (character) {
            '(' => floor += 1,
            ')' => floor -= 1,
            else => {},
        }
    }
    std.debug.print("{d}\n", .{floor});
}

pub fn main() !void {
    // both result in floor 0
    calculateAndPrintFloor("(())");
    calculateAndPrintFloor("()()");

    // both result in floor 3.
    calculateAndPrintFloor("(((");
    calculateAndPrintFloor("(()(()(");

    // also results in floor 3.
    calculateAndPrintFloor("))(((((");

    // both result in floor -1 (the first basement level).
    calculateAndPrintFloor("())");
    calculateAndPrintFloor("))(");

    // both result in floor -3.
    calculateAndPrintFloor(")))");
    calculateAndPrintFloor(")())())");

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const input = try std.fs.cwd().readFileAlloc(allocator, "../input.txt", 1024 * 1024);
    defer allocator.free(input);

    calculateAndPrintFloor(input);
}
