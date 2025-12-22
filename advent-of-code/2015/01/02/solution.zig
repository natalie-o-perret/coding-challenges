const std = @import("std");

fn findAndPrintBasementPosition(source: []const u8) !void {
    var floor: i32 = 0;
    for (source, 0..) |char, index| {
        if (char == '(') {
            floor += 1;
        } else if (char == ')') {
            floor -= 1;
        }

        if (floor == -1) {
            const stdout = std.io.getStdOut().writer();
            try stdout.print("{d}\n", .{index + 1}); // 1-indexed
            break;
        }
    }
}

pub fn main() !void {
    // causes him to enter the basement at character position 1
    try findAndPrintBasementPosition(")");

    // causes him to enter the basement at character position 5
    try findAndPrintBasementPosition("()())");

    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile("../input.txt", .{});
    defer file.close();

    const instructions = try file.readToEndAlloc(allocator, 1024 * 1024);
    defer allocator.free(instructions);

    try findAndPrintBasementPosition(instructions);
}
