const std = @import("std");

fn countHouses(directions: []const u8) !u32 {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var x: i32 = 0;
    var y: i32 = 0;
    var visited = std.AutoHashMap([2]i32, void).init(allocator);
    defer visited.deinit();

    try visited.put([2]i32{ 0, 0 }, {});

    for (directions) |c| {
        switch (c) {
            '^' => y += 1,
            'v' => y -= 1,
            '>' => x += 1,
            '<' => x -= 1,
            else => {},
        }
        try visited.put([2]i32{ x, y }, {});
    }

    return visited.count();
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    // Test cases with assertions
    std.debug.assert(try countHouses(">") == 2);
    std.debug.assert(try countHouses("^>v<") == 4);
    std.debug.assert(try countHouses("^v^v^v^v^v") == 2);

    const input = try std.fs.cwd().readFileAlloc(gpa.allocator(), "../input.txt", 1024 * 1024);
    defer gpa.allocator().free(input);
    const directions = std.mem.trim(u8, input, &std.ascii.whitespace);

    const result = try countHouses(directions);
    std.debug.print("Zig: {d}\n", .{result});
}
