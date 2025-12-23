const std = @import("std");

fn calculateFloor(source: []const u8) i32 {
    var floor: i32 = 0;
    for (source) |character| {
        switch (character) {
            '(' => floor += 1,
            ')' => floor -= 1,
            else => {},
        }
    }
    return floor;
}

pub fn main() !void {
    // Test cases with assertions
    std.debug.assert(calculateFloor("(())") == 0);
    std.debug.assert(calculateFloor("()()") == 0);
    std.debug.assert(calculateFloor("(((") == 3);
    std.debug.assert(calculateFloor("(()(()(") == 3);
    std.debug.assert(calculateFloor("))(((((") == 3);
    std.debug.assert(calculateFloor("())") == -1);
    std.debug.assert(calculateFloor("))(") == -1);
    std.debug.assert(calculateFloor(")))") == -3);
    std.debug.assert(calculateFloor(")())())") == -3);

    // Calculate and print the answer
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const input = try std.fs.cwd().readFileAlloc(allocator, "../input.txt", 1024 * 1024);
    defer allocator.free(input);

    std.debug.print("Zig: {d}\n", .{calculateFloor(input)});
}
