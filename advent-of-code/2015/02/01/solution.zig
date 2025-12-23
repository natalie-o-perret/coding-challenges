const std = @import("std");

fn calculateWrappingPaper(dimensions: []const u8) !u32 {
    var it = std.mem.splitScalar(u8, dimensions, 'x');
    const l = try std.fmt.parseInt(u32, it.next().?, 10);
    const w = try std.fmt.parseInt(u32, it.next().?, 10);
    const h = try std.fmt.parseInt(u32, it.next().?, 10);

    // Calculate surface area
    const surface_area = 2 * l * w + 2 * w * h + 2 * h * l;

    // Find smallest side
    const sides = [_]u32{ l * w, w * h, h * l };
    const slack = @min(@min(sides[0], sides[1]), sides[2]);

    return surface_area + slack;
}

pub fn main() !void {
    // Test cases with assertions
    std.debug.assert(try calculateWrappingPaper("2x3x4") == 58);
    std.debug.assert(try calculateWrappingPaper("1x1x10") == 43);

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const input = try std.fs.cwd().readFileAlloc(allocator, "../input.txt", 1024 * 1024);
    defer allocator.free(input);

    var total: u32 = 0;
    var lines = std.mem.splitScalar(u8, input, '\n');
    while (lines.next()) |line| {
        if (line.len > 0) {
            total += try calculateWrappingPaper(line);
        }
    }
    std.debug.print("Zig: {d}\n", .{total});
}
