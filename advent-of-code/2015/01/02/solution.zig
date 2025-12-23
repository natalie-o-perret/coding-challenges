const std = @import("std");

fn findBasementPosition(source: []const u8) usize {
    var floor: i32 = 0;
    for (source, 0..) |char, index| {
        if (char == '(') {
            floor += 1;
        } else if (char == ')') {
            floor -= 1;
        }

        if (floor == -1) {
            return index + 1; // 1-indexed
        }
    }
    return 0;
}

pub fn main() !void {
    // Test cases with assertions
    std.debug.assert(findBasementPosition(")") == 1);
    std.debug.assert(findBasementPosition("()())") == 5);

    // Calculate and print the answer
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const input = try std.fs.cwd().readFileAlloc(allocator, "../input.txt", 1024 * 1024);
    defer allocator.free(input);

    std.debug.print("Zig: {d}\n", .{findBasementPosition(input)});
}
